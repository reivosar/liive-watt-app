defmodule BackendWeb.Plugs.CORS do
  import Plug.Conn

  def init(default), do: default

  def call(conn, _default) do
    conn
    |> put_resp_header("access-control-allow-origin", "*")
    |> put_resp_header("access-control-allow-methods", "GET, POST, OPTIONS")
    |> put_resp_header("access-control-allow-headers", "Authorization, Content-Type")
  end
end
