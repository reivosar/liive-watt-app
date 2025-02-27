defmodule Backend.EnergyUsageContext do
  import Ecto.Query, warn: false
  alias Backend.Repo
  alias Backend.EnergyUsage
  alias Backend.Prefecture

  def list_energy_usages(filters \\ %{}) do
    query =
      from(e in EnergyUsage,
        join: p in Prefecture,
        on: e.prefecture_code == p.code
      )

    query =
      if has_valid_filters?(filters) do
        query
        |> apply_filters(filters)
        |> add_select_clause()
      else
        query
        |> select_latest_per_prefecture()
      end

    Repo.all(query)
  end

  defp apply_filters(query, filters) do
    Enum.reduce(filters, query, fn
      {:prefecture_name, name}, query when not is_nil(name) and name != "" ->
        from([e, p] in query, where: p.name == ^name)

      {:year, year}, query when not is_nil(year) ->
        from([e, _] in query, where: e.year == ^year)

      {:month, month}, query when not is_nil(month) ->
        from([e, _] in query, where: e.month == ^month)

      _, query ->
        query
    end)
  end

  defp add_select_clause(query) do
    from([e, p] in query,
      select: %{
        prefecture_code: e.prefecture_code,
        prefecture_name: p.name,
        year: e.year,
        month: e.month,
        special_high_voltage_consumption: e.special_high_voltage_consumption,
        special_high_voltage_retailers_count: e.special_high_voltage_retailers_count,
        high_voltage_consumption: e.high_voltage_consumption,
        high_voltage_retailers_count: e.high_voltage_retailers_count,
        low_voltage_consumption: e.low_voltage_consumption,
        low_voltage_special_demand: e.low_voltage_special_demand,
        low_voltage_free_pricing: e.low_voltage_free_pricing,
        low_voltage_retailers_count: e.low_voltage_retailers_count,
        total_consumption: e.total_consumption,
        total_retailers_count: e.total_retailers_count,
        recorded_at: e.recorded_at
      }
    )
  end

  defp has_valid_filters?(filters) do
    filters
    |> Enum.any?(fn {_key, value} -> not is_nil(value) and value != "" end)
  end

  defp select_latest_per_prefecture(query) do
    subquery =
      from(e in EnergyUsage,
        select: %{
          prefecture_code: e.prefecture_code,
          latest_year: max(e.year)
        },
        group_by: e.prefecture_code
      )

    subquery_with_month =
      from(e in EnergyUsage,
        join: s in subquery(subquery),
        on: e.prefecture_code == s.prefecture_code and e.year == s.latest_year,
        select: %{
          prefecture_code: e.prefecture_code,
          latest_year: s.latest_year,
          latest_month: max(e.month)
        },
        group_by: [e.prefecture_code, s.latest_year]
      )

    from([e, p] in query,
      join: s in subquery(subquery_with_month),
      on:
        e.prefecture_code == s.prefecture_code and e.year == s.latest_year and
          e.month == s.latest_month,
      select: %{
        prefecture_code: e.prefecture_code,
        prefecture_name: p.name,
        year: e.year,
        month: e.month,
        special_high_voltage_consumption: e.special_high_voltage_consumption,
        special_high_voltage_retailers_count: e.special_high_voltage_retailers_count,
        high_voltage_consumption: e.high_voltage_consumption,
        high_voltage_retailers_count: e.high_voltage_retailers_count,
        low_voltage_consumption: e.low_voltage_consumption,
        low_voltage_special_demand: e.low_voltage_special_demand,
        low_voltage_free_pricing: e.low_voltage_free_pricing,
        low_voltage_retailers_count: e.low_voltage_retailers_count,
        total_consumption: e.total_consumption,
        total_retailers_count: e.total_retailers_count,
        recorded_at: e.recorded_at
      }
    )
  end
end
