import { combineReducers } from "redux";
import { createDataReducer, createRequestsReducer } from "redux-thunk-data";

export default combineReducers({
  data: createDataReducer(),
  requests: createRequestsReducer(),
});
