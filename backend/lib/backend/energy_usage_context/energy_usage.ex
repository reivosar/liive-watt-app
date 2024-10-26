defmodule Backend.EnergyUsageContext.EnergyUsage do
  use Ecto.Schema
  import Ecto.Changeset

  schema "energy_usages" do
    field(:month, :integer)
    field(:year, :integer)
    field(:prefecture_code, :string)
    field(:special_high_voltage_consumption, :decimal)
    field(:special_high_voltage_retailers_count, :decimal)
    field(:high_voltage_consumption, :decimal)
    field(:high_voltage_retailers_count, :decimal)
    field(:low_voltage_consumption, :decimal)
    field(:low_voltage_special_demand, :decimal)
    field(:low_voltage_free_pricing, :decimal)
    field(:low_voltage_retailers_count, :decimal)
    field(:total_consumption, :decimal)
    field(:total_retailers_count, :decimal)
    field(:recorded_at, :utc_datetime)

    @timestamps_opts [inserted_at: false, updated_at: false]
  end

  @doc false
  def changeset(energy_usage, attrs) do
    energy_usage
    |> cast(attrs, [
      :prefecture_code,
      :year,
      :month,
      :special_high_voltage_consumption,
      :special_high_voltage_retailers_count,
      :high_voltage_consumption,
      :high_voltage_retailers_count,
      :low_voltage_consumption,
      :low_voltage_special_demand,
      :low_voltage_free_pricing,
      :low_voltage_retailers_count,
      :total_consumption,
      :total_retailers_count,
      :recorded_at
    ])
    |> validate_required([
      :prefecture_code,
      :year,
      :month,
      :special_high_voltage_consumption,
      :special_high_voltage_retailers_count,
      :high_voltage_consumption,
      :high_voltage_retailers_count,
      :low_voltage_consumption,
      :low_voltage_special_demand,
      :low_voltage_free_pricing,
      :low_voltage_retailers_count,
      :total_consumption,
      :total_retailers_count,
      :recorded_at
    ])
  end
end
