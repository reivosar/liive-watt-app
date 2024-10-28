export interface EnergyUsage {
  month: number;
  year: number;
  prefecture_name: string;
  prefecture_code: string;
  special_high_voltage_consumption: number;
  special_high_voltage_retailers_count: number;
  high_voltage_consumption: number;
  high_voltage_retailers_count: number;
  low_voltage_consumption: number;
  low_voltage_special_demand: number;
  low_voltage_free_pricing: number;
  low_voltage_retailers_count: number;
  total_consumption: number;
  total_retailers_count: number;
  recorded_at: string;
}
