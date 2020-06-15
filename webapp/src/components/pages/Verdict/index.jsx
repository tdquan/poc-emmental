import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { requestData, selectEntityByKeyAndId } from "redux-thunk-data";

import Header from "components/layout/Header";
import Main from "components/layout/Main";
import VerdictItem from "components/layout/VerdictItem";

import Appearances from "./Appearances";

export default () => {
  const dispatch = useDispatch();
  const { verdictId } = useParams();

  const verdict = useSelector(
    (state) => selectEntityByKeyAndId(state, "verdicts", verdictId),
    [verdictId]
  );
  const { claim } = verdict || {};
  const { quotedFromAppearances } = claim || {};

  useEffect(() => {
    dispatch(requestData({ apiPath: `/verdicts/${verdictId}` }));
  }, [dispatch, verdictId]);

  return (
    <>
      <Header />
      <Main className="verdict">
        <div className="container">
          <VerdictItem className="" verdict={verdict} />
          <Appearances appearances={quotedFromAppearances} />
        </div>
      </Main>
    </>
  );
};
