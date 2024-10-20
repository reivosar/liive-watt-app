defmodule Backend.EnergyUsage do
  use Ecto.Schema
  import Ecto.Changeset

  schema "usages" do
    field :timestamp, :utc_datetime
    field :region, :string
    field :consumption, :float

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(energy_usage, attrs) do
    energy_usage
    |> cast(attrs, [:region, :consumption, :timestamp])
    |> validate_required([:region, :consumption, :timestamp])
  end
end
