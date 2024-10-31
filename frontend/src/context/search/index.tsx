import React, { createContext, useReducer, ReactNode } from "react";
import {
  searchReducer,
  initialState,
  SearchState,
  SearchAction,
} from "../../reducers/searchReducer";

interface SearchContextProps {
  state: SearchState;
  dispatch: React.Dispatch<SearchAction>;
}

interface SearchContextProviderProps {
  children: ReactNode;
}

export const SearchContext = createContext<SearchContextProps | undefined>(
  undefined
);

export const SearchContextProvider: React.FC<SearchContextProviderProps> = ({
  children,
}) => {
  const [state, dispatch] = useReducer(searchReducer, initialState);

  return (
    <SearchContext.Provider value={{ state, dispatch }}>
      {children}
    </SearchContext.Provider>
  );
};
