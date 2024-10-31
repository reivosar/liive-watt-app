import React from "react";
import { EnergyUsage } from "../types/energyUsage";

interface TooltipContentProps {
  consumptionData: EnergyUsage;
}

const TooltipContent: React.FC<TooltipContentProps> = ({ consumptionData }) => {
  return (
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
};

export default TooltipContent;
