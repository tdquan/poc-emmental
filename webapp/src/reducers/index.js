import { combineReducers } from "redux";
// import { createDataReducer } from "redux-thunk-data";

import errors from "./error";
import review from "./review";

export default combineReducers({
  review: review,
  errors: errors,
});
