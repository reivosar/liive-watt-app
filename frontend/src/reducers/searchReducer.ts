import { EnergyUsage } from "../types/energyUsage";

export interface SearchState {
  year: number | null;
  month: number | null;
  data: EnergyUsage[];
  loading: boolean;
  error: string | null;
}

export const initialState: SearchState = {
  year: null,
  month: null,
  data: [],
  loading: false,
  error: null,
};

export enum ActionType {
  SetYear = "SET_YEAR",
  SetMonth = "SET_MONTH",
  FetchDataStart = "FETCH_DATA_START",
  FetchDataSuccess = "FETCH_DATA_SUCCESS",
  FetchDataError = "FETCH_DATA_ERROR",
}

interface SetYearAction {
  type: ActionType.SetYear;
  payload: number;
}

interface SetMonthAction {
  type: ActionType.SetMonth;
  payload: number;
}

interface FetchDataStartAction {
  type: ActionType.FetchDataStart;
}

interface FetchDataSuccessAction {
  type: ActionType.FetchDataSuccess;
  payload: EnergyUsage[];
}

interface FetchDataErrorAction {
  type: ActionType.FetchDataError;
  payload: string;
}

export type SearchAction =
  | SetYearAction
  | SetMonthAction
  | FetchDataStartAction
  | FetchDataSuccessAction
  | FetchDataErrorAction;

export const searchReducer = (
  state: SearchState,
  action: SearchAction
): SearchState => {
  switch (action.type) {
    case ActionType.SetYear:
      return { ...state, year: action.payload };
    case ActionType.SetMonth:
      return { ...state, month: action.payload };
    case ActionType.FetchDataStart:
      return { ...state, loading: true, error: null };
    case ActionType.FetchDataSuccess: {
      const latestData = action.payload[0];
      return {
        ...state,
        data: action.payload,
        year: state.year || latestData?.year,
        month: state.month || latestData?.month,
        loading: false,
      };
    }
    case ActionType.FetchDataError:
      return { ...state, error: action.payload, loading: false };
    default:
      return state;
  }
};
