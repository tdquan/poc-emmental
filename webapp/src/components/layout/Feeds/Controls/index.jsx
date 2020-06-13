import React, { useCallback, useMemo } from "react";
import { useDispatch } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { deleteData, getStateKeyFromConfig } from "redux-thunk-data";

import { ROOT_PATH } from "utils/config";

import KeywordsBar from "./KeywordsBar";
import TagsSelect from "./TagsSelect";

export const getItemsActivityTagFromConfig = (config) =>
  `/${getStateKeyFromConfig(config)}-items`;

export default ({ config }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { pathname, search } = useLocation();
  const url = useMemo(() => new URL(`${ROOT_PATH}${pathname}${search}`), [
    pathname,
    search,
  ]);

  const handleChange = useCallback(
    (key, value) => {
      const isEmptyValue = typeof value === "undefined" || value === "";
      if (isEmptyValue) {
        url.searchParams.delete(key);
      } else {
        url.searchParams.set(key, value);
      }
      if (url.search === search) return;
      dispatch(
        deleteData(null, { tags: [getItemsActivityTagFromConfig(config)] })
      );
      setTimeout(() => history.push("/")); // *TBW*
    },
    [config, dispatch, history, search, url]
  );

  return (
    <div className="controls">
      <TagsSelect
        onChange={handleChange}
        selectedTag={url.searchParams.get("tag")}
      />
      <div className="right">
        <KeywordsBar
          onChange={handleChange}
          selectedKeywords={url.searchParams.get("keywords")} // *TBW*
        />
      </div>
    </div>
  );
};
