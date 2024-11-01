import React from "react";
import CustomMap from "./CustomMap";
import { useSearchContext } from "../context/search/useContext";

const OkinawaMap: React.FC = () => {
  const { state } = useSearchContext();
  const topoUrl = "/topo/okinawa.topojson";

  return (
    <div
      className="absolute bottom-8 right-8"
      style={{ width: "800px", height: "650px" }}
    >
      <CustomMap
        geographyUrl={topoUrl}
        projectionConfig={{
          scale: 7000,
          center: [127.5, 26.5],
        }}
        height={600}
        width={750}
        data={state.data}
      />
    </div>
  );
};

export default OkinawaMap;
