import React from "react";

const Header: React.FC = () => {
  return (
    <header className="bg-black text-white py-4 fixed top-0 left-0 w-full z-50">
      <div className="container mx-auto">
        <h1 className="text-3xl font-bold text-center">
          Japan Electricity Demand Dashboard
        </h1>
      </div>
    </header>
  );
};

export default Header;
