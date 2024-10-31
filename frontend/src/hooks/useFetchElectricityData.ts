import { useState, useEffect } from "react";
import { EnergyUsage } from "../types/energyUsage";
import { get } from "../utils/api";

export const useFetchElectricityData = (url: string) => {
  const [data, setData] = useState<EnergyUsage[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await get<EnergyUsage[]>(url);
        if (response.error) {
          throw new Error(response.error.message);
        }
        if (response.data) {
          setData(response.data);
        }
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
  }, [url]);

  return { data, loading, error };
};
