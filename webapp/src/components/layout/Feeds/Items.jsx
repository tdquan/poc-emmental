import PropTypes from "prop-types";
import React, { useCallback, useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import InfiniteScroll from "react-infinite-scroller";
import {
  getStateKeyFromConfig,
  requestData,
  // selectEntitiesByKeyAndActivityTags,
} from "redux-thunk-data";

import { createCachedSelector } from "re-reselect";

import { getItemsActivityTagFromConfig } from "./Controls";

const REACHABLE_THRESHOLD = -10;
const UNREACHABLE_THRESHOLD = -10000;

const mapArgsToCacheKey = (state, key, tags) => {
  return `${key} ${tags.map((tag) => tag).join(" ")}`;
};

const selectEntitiesByKeyAndActivityTags = createCachedSelector(
  (state, key) => state.data[key],
  (state, key, tags) => tags,
  (entities, tags) => {
    if (!entities) return;
    const tagsLength = tags.length;
    return entities.filter(
      (entity) =>
        tagsLength === entity.__ACTIVITIES__.length &&
        tags.every((tag) => entity.__ACTIVITIES__.includes(tag))
    );
  }
)(mapArgsToCacheKey);

const selectItems = (state, config) =>
  selectEntitiesByKeyAndActivityTags(state, getStateKeyFromConfig(config), [
    getItemsActivityTagFromConfig(config),
  ]);

const selectRequest = (state, config) =>
  state.requests[getItemsActivityTagFromConfig(config)];

const _ = ({ cols, config, renderItem }) => {
  const dispatch = useDispatch();

  const [threshold, setThreshold] = useState(REACHABLE_THRESHOLD);

  const { headers, isPending, isSuccess } =
    useSelector((state) => selectRequest(state, config)) || {};
  const { hasMore = true } = headers || {};

  const items = useSelector((state) => selectItems(state, config));

  const handleGetItems = useCallback(
    (page) => {
      const { apiPath } = config;
      const apiPathWithPage = `${apiPath}${
        apiPath.includes("?") ? "&" : "?"
      }page=${page}`;
      dispatch(
        requestData({
          ...config,
          activityTag: getItemsActivityTagFromConfig(config),
          apiPath: apiPathWithPage,
        })
      );
    },
    [config, dispatch]
  );

  const handleLoadMore = useCallback(
    (page) => {
      if (isPending || !hasMore) return;
      setThreshold(UNREACHABLE_THRESHOLD);
      handleGetItems(page);
    },
    [hasMore, handleGetItems, isPending, setThreshold]
  );

  useEffect(() => {
    handleGetItems(0);
  }, [config, handleGetItems]);

  useEffect(() => {
    if (isSuccess) setThreshold(REACHABLE_THRESHOLD);
  }, [isSuccess]);

  return (
    <InfiniteScroll
      className="items"
      hasMore={hasMore}
      loadMore={handleLoadMore}
      key={config.apiPath}
      threshold={threshold}
      pageStart={0}
      useWindow
    >
      {(items || []).map((item) => (
        <div className={`item-wrapper col-tablet-1of${cols}`} key={item.id}>
          {renderItem(item)}
        </div>
      ))}
    </InfiniteScroll>
  );
};

_.defaultProps = {
  cols: 2,
};

_.propTypes = {
  cols: PropTypes.number,
  config: PropTypes.shape().isRequired,
  renderItem: PropTypes.func.isRequired,
};

export default _;
