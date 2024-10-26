defmodule BackendWeb.EnergyUsageJSON do
  def data(%{
        prefecture_code: prefecture_code,
        prefecture_name: prefecture_name,
        year: year,
        month: month,
        special_high_voltage_consumption: special_high_voltage_consumption,
        special_high_voltage_retailers_count: special_high_voltage_retailers_count,
        high_voltage_consumption: high_voltage_consumption,
        high_voltage_retailers_count: high_voltage_retailers_count,
        low_voltage_consumption: low_voltage_consumption,
        low_voltage_special_demand: low_voltage_special_demand,
        low_voltage_free_pricing: low_voltage_free_pricing,
        low_voltage_retailers_count: low_voltage_retailers_count,
        total_consumption: total_consumption,
        total_retailers_count: total_retailers_count,
        recorded_at: recorded_at
      }) do
    %{
      prefecture_code: prefecture_code,
      prefecture_name: prefecture_name,
      year: year,
      month: month,
      special_high_voltage_consumption: Decimal.to_float(special_high_voltage_consumption),
      special_high_voltage_retailers_count:
        Decimal.to_float(special_high_voltage_retailers_count),
      high_voltage_consumption: Decimal.to_float(high_voltage_consumption),
      high_voltage_retailers_count: Decimal.to_float(high_voltage_retailers_count),
      low_voltage_consumption: Decimal.to_float(low_voltage_consumption),
      low_voltage_special_demand: Decimal.to_float(low_voltage_special_demand),
      low_voltage_free_pricing: Decimal.to_float(low_voltage_free_pricing),
      low_voltage_retailers_count: Decimal.to_float(low_voltage_retailers_count),
      total_consumption: Decimal.to_float(total_consumption),
      total_retailers_count: Decimal.to_float(total_retailers_count),
      recorded_at: recorded_at
    }
  end

  def index(%{energy_usages: energy_usages}) do
    Enum.map(energy_usages, &data/1)
  end
end
