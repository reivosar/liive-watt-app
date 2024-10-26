defmodule BackendWeb.EnergyUsageController do
  use BackendWeb, :controller
  alias Backend.EnergyUsageContext

  def index(conn, params) do
    filters = %{
      prefecture_name: params["prefecture_name"],
      year: params["year"],
      month: params["month"]
    }

    energy_usages = EnergyUsageContext.list_energy_usages(filters)

    render(conn, "index.json", energy_usages: energy_usages)
  end
end
