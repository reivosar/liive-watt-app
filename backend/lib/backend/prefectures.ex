defmodule Backend.Prefecture do
  use Ecto.Schema

  @primary_key {:code, :string, autogenerate: false}
  schema "prefectures" do
    field(:name, :string)

    has_many(:energy_usages, Backend.EnergyUsage, foreign_key: :prefecture_code)

    @timestamps_opts [inserted_at: false, updated_at: false]
  end
end
