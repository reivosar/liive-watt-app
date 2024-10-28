You're right! Here's the updated version with the access information included:

---

# Live Watt App

The **Live Watt App** is a dashboard application to visualize electricity demand across Japan, displaying energy consumption data for each prefecture on a map. The frontend is built using **React**, **Vite**, **TailwindCSS**, and **TypeScript**, and the backend is developed with **Elixir** and **Phoenix**. All components are containerized, allowing for a seamless setup using **Docker**.

## Features

- Interactive map of Japan displaying electricity demand data.
- Energy consumption details displayed in tooltips upon hovering over prefectures.
- Data visualization for specific years and months, with customizable queries.
- Tooltips include detailed breakdowns such as total consumption, special high-voltage consumption, and number of retailers.

## Technology Stack

- **Frontend:**
  - React
  - Vite
  - TypeScript
  - TailwindCSS
  - D3.js for data manipulation and scaling
  - React Simple Maps for map rendering
- **Backend:**
  - Elixir with Phoenix Framework
  - PostgreSQL for data storage

## Prerequisites

- Docker and Docker Compose installed
- `.env` file configured (refer to `.env.example` for environment variables)

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/reivosar/live-watt-app.git
   cd live-watt-app
   ```

2. **Prepare environment variables:**
   Ensure you have an `.env` file in the root directory. You can copy the example configuration from `.env.example`:
   ```bash
   cp .env.example .env
   ```

3. **Build and start the Docker containers:**
   Use Docker Compose to build and start the application. This command will set up both the backend and frontend services:
   ```bash
   docker-compose up --build
   ```

4. **Access the application:**
   Once the containers are running, open a browser and visit `http://localhost:5173/` to access the **Live Watt App** dashboard.

## API Endpoints

- **Energy Usages API:**
  - GET `/api/energy_usages`
  - Allows querying data with optional parameters for `prefectureCode`, `year`, and `month`.

- **Example request:**
  ```bash
  curl http://localhost:4000/api/energy_usages?prefectureCode=13&year=2024&month=3
  ```

Refer to the `.env.example` file for a full list of required environment variables.

## Screenshots

[Add screenshots here to demonstrate the UI and dashboard.]

## Notes

- **No need for `npm run dev`:** The application runs entirely inside Docker containers. Use `docker-compose up --build` to build and run both the frontend and backend.

## License

This project is licensed under the MIT License.

---

Now it clearly states the access URL as `http://localhost:5173/`. Let me know if you'd like any further adjustments!
