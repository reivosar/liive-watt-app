import { useState, useEffect } from "react";
import { EnergyUsage } from "../types/energyUsage";

export const useFetchPrefectureData = (
  prefectureCode: string | null,
  year: number,
  month: number
) => {
  const [data, setData] = useState<EnergyUsage | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!prefectureCode) return;

    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await fetch(
          `http://localhost:4000/api/prefecture/${prefectureCode}?year=${year}&month=${month}`
        );
        if (!response.ok) throw new Error("Failed to fetch prefecture data");
        const result = await response.json();
        setData(result);
      } catch (err) {
        if (err instanceof Error) {
          setError(err.message);
        } else {
          setError("An unknown error occurred");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [prefectureCode, year, month]);

  return { data, loading, error };
};
