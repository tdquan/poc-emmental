import { GET_ERRORS, CLEAR_ERRORS } from "../actions/types";

const initialState = {};

export default (state = initialState, action) => {
  const { type, payload } = action;
  switch (type) {
    case GET_ERRORS:
      return {
        ...state,
        errors: payload,
      };
    case CLEAR_ERRORS:
      return {
        ...state,
        errors: {},
      };
    default:
      return state;
  }
};
