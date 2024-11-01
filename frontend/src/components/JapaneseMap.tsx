import React, { useEffect } from "react";
import { getEnergyUsagesUrl } from "../config";
import { useSearchContext } from "../context/search/useContext";
import { ActionType } from "../reducers/searchReducer";
import { useFetchElectricityData } from "../hooks/useFetchElectricityData";
import CustomMap from "./CustomMap";

const topoUrl = "/topo/japan.topojson";

const JapaneseMap: React.FC = () => {
  const { state, dispatch } = useSearchContext();

  const { data, loading, error } = useFetchElectricityData(
    getEnergyUsagesUrl(
      undefined,
      state.year ?? undefined,
      state.month ?? undefined
    )
  );

  useEffect(() => {
    if (data) {
      dispatch({
        type: ActionType.FetchDataSuccess,
        payload: data,
      });
    }
    if (error) {
      dispatch({
        type: ActionType.FetchDataError,
        payload: error,
      });
    }
  }, [data, error, dispatch]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error fetching data: {state.error}</div>;

  return (
    <div className="relative">
      <CustomMap
        geographyUrl={topoUrl}
        projectionConfig={{
          scale: 980,
          center: [140, 33],
        }}
        height={600}
        width={800}
        data={state.data}
      />
    </div>
  );
};

export default JapaneseMap;
