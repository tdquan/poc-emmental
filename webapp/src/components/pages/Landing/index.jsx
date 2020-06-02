import React, { useEffect, Fragment } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { requestData } from "redux-thunk-data";

import Header from "components/layout/Header";
import Main from "components/layout/Main";

import ReviewItem from "./ReviewItem";

// import { API_URL } from "utils/config";

import { loadReviews } from "actions/review";

const KEYWORDS_CHAIN = "coronavirus";

export default () => {
  const dispatch = useDispatch();

  const reviews = useSelector((state) => state.review.reviews);

  useEffect(() => {
    // const apiPath = `/reviews?keywords=${KEYWORDS_CHAIN}`;
    // dispatch(requestData({ apiPath: apiPath, method: "GET" }));
    dispatch(loadReviews());
  }, [dispatch]);

  return (
    <Fragment>
      <Header />
      <Main className="landing">
        <div className="container">
          <section className="title">
            {`Reviews for "${KEYWORDS_CHAIN}": `}
          </section>
          <section className="results">
            {(reviews || []).map((review, index) => (
              <ReviewItem review={review} key={index} />
            ))}
          </section>
        </div>
      </Main>
    </Fragment>
  );
};
