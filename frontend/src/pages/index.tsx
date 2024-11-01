import React from "react";
import JapaneseMap from "../components/JapaneseMap";
import Header from "../components/Header";
import SearchForm from "../components/SearchForm";
import { SearchContextProvider } from "../context/search";
import ConsumptionBarChart from "../components/ConsumptionBarChart";

const IndexPage: React.FC = () => {
  return (
    <SearchContextProvider>
      <div className="h-screen overflow-hidden bg-gray-100">
        <Header />
        <div className="mt-16">
          <SearchForm />
          <ConsumptionBarChart />
          <JapaneseMap />
        </div>
      </div>
    </SearchContextProvider>
  );
};

export default IndexPage;
