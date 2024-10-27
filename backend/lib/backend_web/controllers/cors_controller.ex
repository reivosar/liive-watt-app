defmodule BackendWeb.CORSController do
  use BackendWeb, :controller

  def options(conn, _params) do
    conn
    |> send_resp(204, "")
  end
end
