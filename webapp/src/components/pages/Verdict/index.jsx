import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { requestData, selectEntityByKeyAndId } from "redux-thunk-data";

import Header from "components/layout/Header";
import Main from "components/layout/Main";
import VerdictItem from "components/layout/VerdictItem";
import selectSortedAppearancesByQuotedClaimId from "selectors/selectSortedAppearancesByQuotedClaimId";

import Appearances from "./Appearances";

export default () => {
  const dispatch = useDispatch();
  const { verdictId } = useParams();

  const verdict = useSelector(
    (state) => selectEntityByKeyAndId(state, "verdicts", verdictId),
    [verdictId]
  );
  const { claimId } = verdict || {};
  const quotedFromAppearances = useSelector((state) =>
    selectSortedAppearancesByQuotedClaimId(state, claimId)
  );

  useEffect(() => {
    dispatch(
      requestData({
        apiPath: `/verdicts/${verdictId}`,
        normalizer: {
          claim: {
            normalizer: {
              quotedFromAppearances: "appearances",
            },
            stateKey: "claims",
          },
        },
      })
    );
  }, [dispatch, verdictId]);

  return (
    <>
      <Header />
      <Main className="verdict">
        <div className="container">
          {verdict && <VerdictItem verdict={verdict} />}
          {quotedFromAppearances && (
            <Appearances appearances={quotedFromAppearances} />
          )}
        </div>
      </Main>
    </>
  );
};
