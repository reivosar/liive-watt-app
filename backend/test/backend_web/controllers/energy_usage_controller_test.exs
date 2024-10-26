defmodule BackendWeb.EnergyUsageControllerTest do
  use BackendWeb.ConnCase

  import Backend.EnergyUsageContextFixtures

  alias Backend.EnergyUsageContext.EnergyUsage

  @create_attrs %{
    month: 42,
    year: 42,
    prefecture_code: "some prefecture_code",
    special_high_voltage_consumption: "120.5",
    special_high_voltage_retailers_count: "120.5",
    high_voltage_consumption: "120.5",
    high_voltage_retailers_count: "120.5",
    low_voltage_consumption: "120.5",
    low_voltage_special_demand: "120.5",
    low_voltage_free_pricing: "120.5",
    low_voltage_retailers_count: "120.5",
    total_consumption: "120.5",
    total_retailers_count: "120.5",
    recorded_at: ~U[2024-10-25 18:20:00Z]
  }
  @update_attrs %{
    month: 43,
    year: 43,
    prefecture_code: "some updated prefecture_code",
    special_high_voltage_consumption: "456.7",
    special_high_voltage_retailers_count: "456.7",
    high_voltage_consumption: "456.7",
    high_voltage_retailers_count: "456.7",
    low_voltage_consumption: "456.7",
    low_voltage_special_demand: "456.7",
    low_voltage_free_pricing: "456.7",
    low_voltage_retailers_count: "456.7",
    total_consumption: "456.7",
    total_retailers_count: "456.7",
    recorded_at: ~U[2024-10-26 18:20:00Z]
  }
  @invalid_attrs %{month: nil, year: nil, prefecture_code: nil, special_high_voltage_consumption: nil, special_high_voltage_retailers_count: nil, high_voltage_consumption: nil, high_voltage_retailers_count: nil, low_voltage_consumption: nil, low_voltage_special_demand: nil, low_voltage_free_pricing: nil, low_voltage_retailers_count: nil, total_consumption: nil, total_retailers_count: nil, recorded_at: nil}

  setup %{conn: conn} do
    {:ok, conn: put_req_header(conn, "accept", "application/json")}
  end

  describe "index" do
    test "lists all energy_usages", %{conn: conn} do
      conn = get(conn, ~p"/api/energy_usages")
      assert json_response(conn, 200)["data"] == []
    end
  end

  describe "create energy_usage" do
    test "renders energy_usage when data is valid", %{conn: conn} do
      conn = post(conn, ~p"/api/energy_usages", energy_usage: @create_attrs)
      assert %{"id" => id} = json_response(conn, 201)["data"]

      conn = get(conn, ~p"/api/energy_usages/#{id}")

      assert %{
               "id" => ^id,
               "high_voltage_consumption" => "120.5",
               "high_voltage_retailers_count" => "120.5",
               "low_voltage_consumption" => "120.5",
               "low_voltage_free_pricing" => "120.5",
               "low_voltage_retailers_count" => "120.5",
               "low_voltage_special_demand" => "120.5",
               "month" => 42,
               "prefecture_code" => "some prefecture_code",
               "recorded_at" => "2024-10-25T18:20:00Z",
               "special_high_voltage_consumption" => "120.5",
               "special_high_voltage_retailers_count" => "120.5",
               "total_consumption" => "120.5",
               "total_retailers_count" => "120.5",
               "year" => 42
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn} do
      conn = post(conn, ~p"/api/energy_usages", energy_usage: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "update energy_usage" do
    setup [:create_energy_usage]

    test "renders energy_usage when data is valid", %{conn: conn, energy_usage: %EnergyUsage{id: id} = energy_usage} do
      conn = put(conn, ~p"/api/energy_usages/#{energy_usage}", energy_usage: @update_attrs)
      assert %{"id" => ^id} = json_response(conn, 200)["data"]

      conn = get(conn, ~p"/api/energy_usages/#{id}")

      assert %{
               "id" => ^id,
               "high_voltage_consumption" => "456.7",
               "high_voltage_retailers_count" => "456.7",
               "low_voltage_consumption" => "456.7",
               "low_voltage_free_pricing" => "456.7",
               "low_voltage_retailers_count" => "456.7",
               "low_voltage_special_demand" => "456.7",
               "month" => 43,
               "prefecture_code" => "some updated prefecture_code",
               "recorded_at" => "2024-10-26T18:20:00Z",
               "special_high_voltage_consumption" => "456.7",
               "special_high_voltage_retailers_count" => "456.7",
               "total_consumption" => "456.7",
               "total_retailers_count" => "456.7",
               "year" => 43
             } = json_response(conn, 200)["data"]
    end

    test "renders errors when data is invalid", %{conn: conn, energy_usage: energy_usage} do
      conn = put(conn, ~p"/api/energy_usages/#{energy_usage}", energy_usage: @invalid_attrs)
      assert json_response(conn, 422)["errors"] != %{}
    end
  end

  describe "delete energy_usage" do
    setup [:create_energy_usage]

    test "deletes chosen energy_usage", %{conn: conn, energy_usage: energy_usage} do
      conn = delete(conn, ~p"/api/energy_usages/#{energy_usage}")
      assert response(conn, 204)

      assert_error_sent 404, fn ->
        get(conn, ~p"/api/energy_usages/#{energy_usage}")
      end
    end
  end

  defp create_energy_usage(_) do
    energy_usage = energy_usage_fixture()
    %{energy_usage: energy_usage}
  end
end
