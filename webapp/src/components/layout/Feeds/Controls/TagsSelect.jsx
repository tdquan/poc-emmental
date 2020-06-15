import PropTypes from "prop-types";
import React, { useCallback, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { requestData } from "redux-thunk-data";

const _ = ({ onChange, selectedTag }) => {
  const dispatch = useDispatch();

  const tags = useSelector((state) => state.data.tags);

  const handleOnChange = useCallback(
    (event) => onChange("tag", event.target.value),
    [onChange]
  );

  useEffect(() => {
    dispatch(requestData({ apiPath: "/tags" }));
  }, [dispatch]);

  if (!tags) return null;

  return (
    <select
      className="tags-select"
      onChange={handleOnChange}
      value={selectedTag || ""}
    >
      <option key={""} value={""}>
        All Tags
      </option>
      {tags.map(({ label }) => (
        <option key={label} value={label}>
          {label}
        </option>
      ))}
    </select>
  );
};

_.propTypes = {
  onChange: PropTypes.func.isRequired,
  selectedTag: PropTypes.string,
};

export default _;
