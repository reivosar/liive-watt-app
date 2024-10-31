import React from "react";
import { useSearchContext } from "../context/search/useContext";
import "react-datepicker/dist/react-datepicker.css";
import { ActionType } from "../reducers/searchReducer";
import CustomDatePicker from "./CustomDatePicker";

const SearchForm: React.FC = () => {
  const { state, dispatch } = useSearchContext();

  const handleDateChange = (dates: Date[]) => {
    const date = dates[0] || null;
    if (date) {
      const year = date.getFullYear();
      const month = date.getMonth() + 1;

      dispatch({ type: ActionType.SetYear, payload: year });
      dispatch({ type: ActionType.SetMonth, payload: month });
    }
  };

  return (
    <div className="absolute left-10 top-[80px] bg-white p-4 rounded-lg shadow-lg z-50 flex items-center space-x-4">
      <select
        value={state.year ?? ""}
        onChange={(e) =>
          dispatch({
            type: ActionType.SetYear,
            payload: Number(e.target.value),
          })
        }
        className="border border-gray-300 p-2 rounded-md text-lg"
      >
        <option value="">年を選択</option>
        {Array.from({ length: 5 }, (_, i) => (
          <option key={i} value={2024 - i}>
            {2024 - i}
          </option>
        ))}
      </select>

      <select
        value={state.month ?? ""}
        onChange={(e) =>
          dispatch({
            type: ActionType.SetMonth,
            payload: Number(e.target.value),
          })
        }
        className="border border-gray-300 p-2 rounded-md text-lg"
      >
        <option value="">月を選択</option>
        {Array.from({ length: 12 }, (_, i) => (
          <option key={i + 1} value={i + 1}>
            {String(i + 1).padStart(2, "0")}
          </option>
        ))}
      </select>

      <CustomDatePicker
        selectedDate={
          state.year && state.month
            ? new Date(state.year, state.month - 1)
            : null
        }
        onChange={handleDateChange}
      />
    </div>
  );
};

export default SearchForm;
