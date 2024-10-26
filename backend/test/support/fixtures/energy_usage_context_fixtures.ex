defmodule Backend.EnergyUsageContextFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `Backend.EnergyUsageContext` context.
  """

  @doc """
  Generate a energy_usage.
  """
  def energy_usage_fixture(attrs \\ %{}) do
    {:ok, energy_usage} =
      attrs
      |> Enum.into(%{
        high_voltage_consumption: "120.5",
        high_voltage_retailers_count: "120.5",
        low_voltage_consumption: "120.5",
        low_voltage_free_pricing: "120.5",
        low_voltage_retailers_count: "120.5",
        low_voltage_special_demand: "120.5",
        month: 42,
        prefecture_code: "some prefecture_code",
        recorded_at: ~U[2024-10-25 18:20:00Z],
        special_high_voltage_consumption: "120.5",
        special_high_voltage_retailers_count: "120.5",
        total_consumption: "120.5",
        total_retailers_count: "120.5",
        year: 42
      })
      |> Backend.EnergyUsageContext.create_energy_usage()

    energy_usage
  end
end
