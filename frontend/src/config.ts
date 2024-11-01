export const getBackendUrl = (): string => {
  const hostName = import.meta.env.VITE_BACKEND_URL;
  return "http://localhost:4000";
};

export const getEnergyUsagesUrl = (
  prefectureCode?: string,
  year?: number,
  month?: number
): string => {
  let url = `${getBackendUrl()}/api/energy_usages`;

  if (prefectureCode) {
    url += `/${prefectureCode}`;
  }

  const queryParams: string[] = [];
  if (year) {
    queryParams.push(`year=${year}`);
  }
  if (month) {
    queryParams.push(`month=${month}`);
  }

  if (queryParams.length > 0) {
    url += `?${queryParams.join("&")}`;
  }

  return url;
};
