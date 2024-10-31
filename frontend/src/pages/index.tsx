import React from "react";
import JapaneseMap from "../components/JapaneseMap";
import Header from "../components/Header";
import SearchForm from "../components/SearchForm";
import { SearchContextProvider } from "../context/search";

const IndexPage: React.FC = () => {
  return (
    <SearchContextProvider>
      <div className="h-screen overflow-hidden bg-gray-100">
        <Header />
        <div className="mt-16">
          <SearchForm />
          <JapaneseMap />
        </div>
      </div>
    </SearchContextProvider>
  );
};

export default IndexPage;
