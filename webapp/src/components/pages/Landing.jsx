import React, { useCallback } from "react";
import { useHistory } from "react-router-dom";

import Header from "components/layout/Header";
import KeywordsBar from "components/layout/Feeds/Controls/KeywordsBar";
import Main from "components/layout/Main";

export default () => {
  const history = useHistory();

  const handleChange = useCallback(
    (key, value) => history.push(`/verdicts?keywords=${value}`),
    [history]
  );

  return (
    <>
      <Header />
      <Main className="landing">
        <div className="container">
          <div className="title">Welcome to the Poc Challenge !</div>
          <div className="cta">
            <KeywordsBar onChange={handleChange} />
          </div>
        </div>
      </Main>
    </>
  );
};
