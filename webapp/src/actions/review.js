import { API_URL } from "utils/config";
import { LOAD_REVIEWS, GET_ERRORS } from "./types";

const KEYWORDS_CHAIN = "coronavirus";

export const loadReviews = () => async (dispatch) => {
  const headers = {
    "Content-Type": "application/json",
    Accept: "application/json",
  };

  const config = {
    method: "GET",
    headers: headers,
  };

  const apiPath = `${API_URL}/reviews?keywords=${KEYWORDS_CHAIN}`;

  const res = await fetch(apiPath, config);

  res
    .json()
    .then((data) =>
      dispatch({
        type: LOAD_REVIEWS,
        payload: data,
      })
    )
    .catch((err) =>
      dispatch({
        type: GET_ERRORS,
        payload: err,
      })
    );
};
