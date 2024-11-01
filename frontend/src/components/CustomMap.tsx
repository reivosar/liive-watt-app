import React, { useState } from "react";
import { ComposableMap, Geographies, Geography } from "react-simple-maps";
import { EnergyUsage } from "../types/energyUsage";
import TooltipContent from "./TooltipContent";
import { scaleLinear } from "d3-scale";

interface CustomMapProps {
  geographyUrl: string;
  projectionConfig: {
    scale: number;
    center: [number, number];
  };
  height: number;
  width: number;
  data: EnergyUsage[];
}

const colorScale = scaleLinear<string>()
  .domain([0, 10000000])
  .range(["#E0F7FA", "#006064"]);

const CustomMap: React.FC<CustomMapProps> = ({
  geographyUrl,
  projectionConfig,
  height,
  width,
  data,
}) => {
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
          x: targetRect.right - 180,
          y: targetRect.bottom - 120,
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

  return (
    <div className="relative">
      <ComposableMap
        projection="geoMercator"
        projectionConfig={projectionConfig}
        height={height}
        width={width}
      >
        <Geographies geography={geographyUrl}>
          {({ geographies }) =>
            geographies.map((geo) => {
              const prefectureName = geo.properties.nam_ja;
              const consumptionData = data.find(
                (d) => d.prefecture_name === prefectureName
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

export default CustomMap;
