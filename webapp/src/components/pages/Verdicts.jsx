import React, { useCallback, useMemo } from "react";
import { useLocation } from "react-router-dom";

import Feeds from "components/layout/Feeds";
import Header from "components/layout/Header";
import Main from "components/layout/Main";

import VerdictItem from "components/layout/VerdictItem";

export default () => {
  const { search } = useLocation();

  const config = useMemo(
    () => ({
      apiPath: `/verdicts${search}`,
    }),
    [search]
  );

  const renderItem = useCallback(
    (item) => <VerdictItem className="clickable" verdict={item} />,
    []
  );

  return (
    <>
      <Header />
      <Main className="verdicts">
        <div className="container">
          <section className="title">Verdicts found</section>
          <section className="results">
            <Feeds config={config} key={search} renderItem={renderItem} />
          </section>
        </div>
      </Main>
    </>
  );
};
