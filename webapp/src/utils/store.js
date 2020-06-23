import { compose, createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

import rootReducer from "reducers";

import { API_URL } from "./config";

const buildStoreEnhancer = (middlewares = []) => {
  const enhancers = [];

  const useDevTools =
    typeof window !== "undefined" &&
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__;

  if (useDevTools) {
    const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__;
    return composeEnhancers(...enhancers, applyMiddleware(...middlewares));
  }

  return compose(...enhancers, applyMiddleware(...middlewares));
};

export default (initialState = {}) => {
  const middlewares = [thunk.withExtraArgument({ rootUrl: API_URL })];

  const storeEnhancer = buildStoreEnhancer(middlewares);

  const store = createStore(rootReducer, storeEnhancer);

  return { store };
};
