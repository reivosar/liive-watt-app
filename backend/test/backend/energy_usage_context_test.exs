defmodule Backend.EnergyUsageContextTest do
  use Backend.DataCase

  alias Backend.EnergyUsageContext

  describe "energy_usages" do
    alias Backend.EnergyUsageContext.EnergyUsage

    import Backend.EnergyUsageContextFixtures

    @invalid_attrs %{month: nil, year: nil, prefecture_code: nil, special_high_voltage_consumption: nil, special_high_voltage_retailers_count: nil, high_voltage_consumption: nil, high_voltage_retailers_count: nil, low_voltage_consumption: nil, low_voltage_special_demand: nil, low_voltage_free_pricing: nil, low_voltage_retailers_count: nil, total_consumption: nil, total_retailers_count: nil, recorded_at: nil}

    test "list_energy_usages/0 returns all energy_usages" do
      energy_usage = energy_usage_fixture()
      assert EnergyUsageContext.list_energy_usages() == [energy_usage]
    end

    test "get_energy_usage!/1 returns the energy_usage with given id" do
      energy_usage = energy_usage_fixture()
      assert EnergyUsageContext.get_energy_usage!(energy_usage.id) == energy_usage
    end

    test "create_energy_usage/1 with valid data creates a energy_usage" do
      valid_attrs = %{month: 42, year: 42, prefecture_code: "some prefecture_code", special_high_voltage_consumption: "120.5", special_high_voltage_retailers_count: "120.5", high_voltage_consumption: "120.5", high_voltage_retailers_count: "120.5", low_voltage_consumption: "120.5", low_voltage_special_demand: "120.5", low_voltage_free_pricing: "120.5", low_voltage_retailers_count: "120.5", total_consumption: "120.5", total_retailers_count: "120.5", recorded_at: ~U[2024-10-25 18:20:00Z]}

      assert {:ok, %EnergyUsage{} = energy_usage} = EnergyUsageContext.create_energy_usage(valid_attrs)
      assert energy_usage.month == 42
      assert energy_usage.year == 42
      assert energy_usage.prefecture_code == "some prefecture_code"
      assert energy_usage.special_high_voltage_consumption == Decimal.new("120.5")
      assert energy_usage.special_high_voltage_retailers_count == Decimal.new("120.5")
      assert energy_usage.high_voltage_consumption == Decimal.new("120.5")
      assert energy_usage.high_voltage_retailers_count == Decimal.new("120.5")
      assert energy_usage.low_voltage_consumption == Decimal.new("120.5")
      assert energy_usage.low_voltage_special_demand == Decimal.new("120.5")
      assert energy_usage.low_voltage_free_pricing == Decimal.new("120.5")
      assert energy_usage.low_voltage_retailers_count == Decimal.new("120.5")
      assert energy_usage.total_consumption == Decimal.new("120.5")
      assert energy_usage.total_retailers_count == Decimal.new("120.5")
      assert energy_usage.recorded_at == ~U[2024-10-25 18:20:00Z]
    end

    test "create_energy_usage/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = EnergyUsageContext.create_energy_usage(@invalid_attrs)
    end

    test "update_energy_usage/2 with valid data updates the energy_usage" do
      energy_usage = energy_usage_fixture()
      update_attrs = %{month: 43, year: 43, prefecture_code: "some updated prefecture_code", special_high_voltage_consumption: "456.7", special_high_voltage_retailers_count: "456.7", high_voltage_consumption: "456.7", high_voltage_retailers_count: "456.7", low_voltage_consumption: "456.7", low_voltage_special_demand: "456.7", low_voltage_free_pricing: "456.7", low_voltage_retailers_count: "456.7", total_consumption: "456.7", total_retailers_count: "456.7", recorded_at: ~U[2024-10-26 18:20:00Z]}

      assert {:ok, %EnergyUsage{} = energy_usage} = EnergyUsageContext.update_energy_usage(energy_usage, update_attrs)
      assert energy_usage.month == 43
      assert energy_usage.year == 43
      assert energy_usage.prefecture_code == "some updated prefecture_code"
      assert energy_usage.special_high_voltage_consumption == Decimal.new("456.7")
      assert energy_usage.special_high_voltage_retailers_count == Decimal.new("456.7")
      assert energy_usage.high_voltage_consumption == Decimal.new("456.7")
      assert energy_usage.high_voltage_retailers_count == Decimal.new("456.7")
      assert energy_usage.low_voltage_consumption == Decimal.new("456.7")
      assert energy_usage.low_voltage_special_demand == Decimal.new("456.7")
      assert energy_usage.low_voltage_free_pricing == Decimal.new("456.7")
      assert energy_usage.low_voltage_retailers_count == Decimal.new("456.7")
      assert energy_usage.total_consumption == Decimal.new("456.7")
      assert energy_usage.total_retailers_count == Decimal.new("456.7")
      assert energy_usage.recorded_at == ~U[2024-10-26 18:20:00Z]
    end

    test "update_energy_usage/2 with invalid data returns error changeset" do
      energy_usage = energy_usage_fixture()
      assert {:error, %Ecto.Changeset{}} = EnergyUsageContext.update_energy_usage(energy_usage, @invalid_attrs)
      assert energy_usage == EnergyUsageContext.get_energy_usage!(energy_usage.id)
    end

    test "delete_energy_usage/1 deletes the energy_usage" do
      energy_usage = energy_usage_fixture()
      assert {:ok, %EnergyUsage{}} = EnergyUsageContext.delete_energy_usage(energy_usage)
      assert_raise Ecto.NoResultsError, fn -> EnergyUsageContext.get_energy_usage!(energy_usage.id) end
    end

    test "change_energy_usage/1 returns a energy_usage changeset" do
      energy_usage = energy_usage_fixture()
      assert %Ecto.Changeset{} = EnergyUsageContext.change_energy_usage(energy_usage)
    end
  end
end
