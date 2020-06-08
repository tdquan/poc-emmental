import { LOAD_REVIEWS } from "../actions/types";

const initialState = {
  reviews: [],
  loading: true,
};

export default (state = initialState, action) => {
  const { type, payload } = action;
  switch (type) {
    case LOAD_REVIEWS:
      return {
        ...state,
        reviews: payload,
        loading: false,
      };
    default:
      return {
        ...state,
        loading: false,
      };
  }
};
