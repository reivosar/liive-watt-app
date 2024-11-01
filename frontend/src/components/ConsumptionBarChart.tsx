import React from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { useSearchContext } from "../context/search/useContext";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const ConsumptionBarChart: React.FC = () => {
  const { state } = useSearchContext();

  const sortedData = state.data
    .sort((a, b) => b.total_consumption - a.total_consumption)
    .slice(0, 5);

  const chartData = {
    labels: sortedData.map((item) => item.prefecture_name),
    datasets: [
      {
        label: "電力需要量(kW)",
        data: sortedData.map((item) => item.total_consumption / 1000),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
        borderColor: "rgba(75, 192, 192, 1)",
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    indexAxis: "y" as const,
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: "top" as const,
      },
      title: {
        display: true,
        text: "都道府県別電力需要量トップ5",
      },
    },
  };

  return (
    <div
      className="absolute left-10 top-[calc(80px+4rem)] bg-white p-4 rounded-lg shadow-lg z-50 mt-4"
      style={{ height: "300px", width: "550px" }}
    >
      <Bar data={chartData} options={chartOptions} />
    </div>
  );
};

export default ConsumptionBarChart;
