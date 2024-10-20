import Config

# Configure your database
config :backend, Backend.Repo,
  username: System.get_env("POSTGRES_USER") || "postgres",
  password: System.get_env("POSTGRES_PASSWORD") || "postgres",
  hostname: System.get_env("DB_HOST") || "localhost",
  database: System.get_env("POSTGRES_DB") || "live_watt_db",
  port: String.to_integer(System.get_env("DB_PORT") || "5432"),
  stacktrace: true,
  show_sensitive_data_on_connection_error: true,
  pool_size: 10

# Development configuration
config :backend, BackendWeb.Endpoint,
  http: [
    ip: {0, 0, 0, 0},
    port: String.to_integer(System.get_env("BACKEND_PORT") || "4000")
  ],
  check_origin: false,
  code_reloader: true,
  debug_errors: true,
  secret_key_base:
    System.get_env("SECRET_KEY_BASE") ||
      "CVnqSdhS4wjCjIPmGTC0+yOTG3OdBcxo1cDGAw5/Gdyn5VUclUIS2zDFL+YBqt2l",
  watchers: [
    esbuild: {Esbuild, :install_and_run, [:backend, ~w(--sourcemap=inline --watch)]},
    tailwind: {Tailwind, :install_and_run, [:backend, ~w(--watch)]}
  ]

# Static and templates reloading configuration
config :backend, BackendWeb.Endpoint,
  live_reload: [
    patterns: [
      ~r"priv/static/(?!uploads/).*(js|css|png|jpeg|jpg|gif|svg)$",
      ~r"priv/gettext/.*(po)$",
      ~r"lib/backend_web/(controllers|live|components)/.*(ex|heex)$"
    ]
  ]

# Enable dev routes for dashboard and mailbox
config :backend, dev_routes: true

# Logger configuration
config :logger, :console, format: "[$level] $message\n"

# Development stacktrace configuration
config :phoenix, :stacktrace_depth, 20

# Initialize plugs at runtime for faster development compilation
config :phoenix, :plug_init_mode, :runtime

# Phoenix LiveView debugging
config :phoenix_live_view,
  debug_heex_annotations: true,
  enable_expensive_runtime_checks: true

# Disable Swoosh API client for development
config :swoosh, :api_client, false
