import React, { useRef } from "react";
import Flatpickr from "react-flatpickr";
import "flatpickr/dist/flatpickr.min.css";
import "flatpickr/dist/plugins/monthSelect/style.css";
import { FaCalendarAlt } from "react-icons/fa";
import monthSelectPlugin from "flatpickr/dist/plugins/monthSelect";
import { Japanese } from "flatpickr/dist/l10n/ja.js";

interface CustomDatePickerProps {
  selectedDate: Date | null;
  onChange: (date: Date[]) => void;
}

const CustomDatePicker: React.FC<CustomDatePickerProps> = ({
  selectedDate,
  onChange,
}) => {
  const flatpickrRef = useRef<Flatpickr | null>(null);

  const handleIconClick = () => {
    if (flatpickrRef.current?.flatpickr) {
      flatpickrRef.current.flatpickr.open();
    }
  };

  const handleDateChange = (dates: Date[]) => {
    if (dates.length > 0) {
      onChange(dates);
    }
  };

  return (
    <div className="relative flex items-center">
      <Flatpickr
        ref={flatpickrRef}
        value={selectedDate ? selectedDate : undefined}
        onChange={handleDateChange}
        options={{
          locale: Japanese,
          dateFormat: "Y/m",
          plugins: [
            monthSelectPlugin({
              shorthand: true,
              dateFormat: "Y/m",
              theme: "light",
            }),
          ],
        }}
        className="hidden"
      />
      <button
        onClick={handleIconClick}
        className="ml-2 bg-white border border-gray-300 hover:bg-blue-100 p-2 rounded-md shadow-md transition-all duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-blue-400"
      >
        <FaCalendarAlt size={24} />
      </button>
    </div>
  );
};

export default CustomDatePicker;
