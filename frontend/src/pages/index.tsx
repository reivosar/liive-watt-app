import React from "react";
import JapaneseMap from "../components/JapaneseMap";
import Header from "../components/Header";

const IndexPage: React.FC = () => {
  return (
    <div className="h-screen overflow-hidden bg-gray-100">
      <Header />
      <div className="mt-16">
        <JapaneseMap />
      </div>
    </div>
  );
};

export default IndexPage;
