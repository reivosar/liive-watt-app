import React, { useEffect, useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { scaleLinear } from "d3-scale";
import { prefectureMapping } from "../data/prefectures";
import { EnergyUsage } from "../types/energyUsage";
import { getEnergyUsagesUrl } from "../config";
import { useSearchContext } from "../context/search/useContext";
import TooltipContent from "./TooltipContent";
import { ActionType } from "../reducers/searchReducer";
import { useFetchElectricityData } from "../hooks/useFetchElectricityData";

const topoUrl = "/topo/japan.topojson";

const colorScale = scaleLinear<string>()
  .domain([0, 7000000])
  .range(["#E0F7FA", "#006064"]);

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

  const [tooltipContent, setTooltipContent] = useState<JSX.Element | null>(
    null
  );
  const [tooltipPosition, setTooltipPosition] = useState({ x: 0, y: 0 });

  const handleMouseEnter = (
    event: React.MouseEvent,
    consumptionData: EnergyUsage | undefined
  ) => {
    if (consumptionData) {
      const content = <TooltipContent consumptionData={consumptionData} />;
      setTooltipContent(content);

      const targetRect = event.currentTarget.getBoundingClientRect();
      if (consumptionData.prefecture_name === "北海道") {
        setTooltipPosition({
          x: targetRect.right - 230,
          y: targetRect.bottom - 160,
        });
      } else {
        setTooltipPosition({
          x: targetRect.left + 100,
          y: targetRect.top - 200,
        });
      }
    }
  };

  const handleMouseLeave = () => {
    setTooltipContent(null);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error fetching data: {state.error}</div>;

  return (
    <div className="relative">
      <ComposableMap
        projection="geoMercator"
        projectionConfig={{
          scale: 980,
          center: [140, 33],
        }}
        height={600}
        width={800}
      >
        <Geographies geography={topoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => {
              const prefectureCode = (
                Object.keys(
                  prefectureMapping
                ) as (keyof typeof prefectureMapping)[]
              ).find(
                (code) => prefectureMapping[code] === geo.properties.nam_ja
              );

              const consumptionData = state.data.find(
                (d) => d.prefecture_code === prefectureCode
              );

              return (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  fill={
                    consumptionData
                      ? colorScale(consumptionData.total_consumption)
                      : "#EEE"
                  }
                  stroke="#FFF"
                  className="transition duration-300 ease-in-out hover:fill-blue-600"
                  onMouseEnter={(event) =>
                    handleMouseEnter(event, consumptionData)
                  }
                  onMouseLeave={handleMouseLeave}
                />
              );
            })
          }
        </Geographies>
      </ComposableMap>

      {tooltipContent && (
        <div
          className="absolute bg-white text-black p-2 rounded shadow-lg"
          style={{
            top: tooltipPosition.y,
            left: tooltipPosition.x,
            pointerEvents: "none",
            whiteSpace: "nowrap",
            zIndex: 1000,
          }}
        >
          {tooltipContent}
        </div>
      )}
    </div>
  );
};

export default JapaneseMap;
