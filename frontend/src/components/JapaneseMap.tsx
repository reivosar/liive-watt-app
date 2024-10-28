import React, { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { scaleLinear } from "d3-scale";
import { useFetchElectricityData } from "../hooks/useFetchElectricityData";
import { prefectureMapping } from "../data/prefectures";
import { EnergyUsage } from "../types/energyUsage";

const topoUrl = "/topo/japan.topojson";

const colorScale = scaleLinear<string>()
  .domain([0, 7000000])
  .range(["#E0F7FA", "#006064"]);

const JapaneseMap: React.FC = () => {
  const { data, loading, error } = useFetchElectricityData(
    "http://localhost:4000/api/energy_usages"
  );

  const [tooltipContent, setTooltipContent] = useState<JSX.Element | null>(
    null
  );
  const [tooltipPosition, setTooltipPosition] = useState({ x: 0, y: 0 });

  const handleMouseEnter = (
    event: React.MouseEvent,
    consumptionData: EnergyUsage | undefined
  ) => {
    if (consumptionData) {
      const content = (
        <table className="min-w-max text-sm text-left">
          <tbody>
            <tr>
              <td className="font-bold pr-2">都道府県:</td>
              <td>{consumptionData.prefecture_name}</td>
            </tr>
            <tr>
              <td className="font-bold pr-2">年:</td>
              <td>{consumptionData.year}</td>
            </tr>
            <tr>
              <td className="font-bold pr-2">月:</td>
              <td>{consumptionData.month}</td>
            </tr>
            <tr>
              <td className="font-bold pr-2">合計消費量:</td>
              <td>{consumptionData.total_consumption.toLocaleString()} kWh</td>
            </tr>
            <tr>
              <td className="font-bold pr-2">小売事業者数:</td>
              <td>{consumptionData.total_retailers_count}</td>
            </tr>
            <tr>
              <td className="font-bold pr-2">特別高圧消費量:</td>
              <td>
                {consumptionData.special_high_voltage_consumption.toLocaleString()}{" "}
                kWh
              </td>
            </tr>
            <tr>
              <td className="font-bold pr-2">高圧消費量:</td>
              <td>
                {consumptionData.high_voltage_consumption.toLocaleString()} kWh
              </td>
            </tr>
            <tr>
              <td className="font-bold pr-2">低圧消費量:</td>
              <td>
                {consumptionData.low_voltage_consumption.toLocaleString()} kWh
              </td>
            </tr>
          </tbody>
        </table>
      );
      setTooltipContent(content);

      const targetRect = event.currentTarget.getBoundingClientRect();
      if (consumptionData.prefecture_name === "北海道") {
        setTooltipPosition({
          x: targetRect.right - 200,
          y: targetRect.bottom - 125,
        });
      } else {
        setTooltipPosition({
          x: targetRect.right + 50,
          y: targetRect.top - 200,
        });
      }
    }
  };

  const handleMouseLeave = () => {
    setTooltipContent(null);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error fetching data: {error}</div>;

  return (
    <div className="relative">
      <ComposableMap
        projection="geoMercator"
        projectionConfig={{
          scale: 1000,
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

              const consumptionData = data.find(
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
