FROM elixir:1.14-alpine

RUN apk add --no-cache build-base npm git inotify-tools

WORKDIR /app

COPY mix.exs mix.lock ./
RUN mix local.hex --force && \
    mix local.rebar --force && \
    mix deps.get

COPY . .