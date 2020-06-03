import React, { useEffect, Fragment } from "react";
import { useDispatch, useSelector } from "react-redux";
import { requestData } from "redux-thunk-data";

import Header from "components/layout/Header";
import Main from "components/layout/Main";

import ReviewItem from "./ReviewItem";

// import { loadReviews } from "actions/review";

const KEYWORDS_CHAIN = "coronavirus";

export default () => {
  const dispatch = useDispatch();

  const reviews = useSelector((state) => state.data.reviews);

  useEffect(() => {
    const apiPath = `/reviews?keywords=${KEYWORDS_CHAIN}`;
    dispatch(requestData({ apiPath }));
    // dispatch(loadReviews());
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
