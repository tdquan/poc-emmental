import classnames from "classnames";
import PropTypes from "prop-types";
import React, { useCallback } from "react";
import { useHistory } from "react-router-dom";
import { useSelector } from "react-redux";

import { selectEntityByKeyAndId } from "redux-thunk-data";

const _ = ({ className, verdict }) => {
  const { claimId, editor, id, verdictTags, title: headline } = verdict;
  const claim = useSelector(
    (state) => selectEntityByKeyAndId(state, "claims", claimId),
    [claimId]
  );
  // const { quotedFromAppearances } = claim || {};

  const history = useHistory();

  const handleClick = useCallback(() => history.push(`/verdicts/${id}`), [
    history,
    id,
  ]);

  return (
    <div
      className={classnames("verdict-item", className)}
      onClick={handleClick}
    >
      <div className="text-muted">
        editor: {`${editor.firstName} ${editor.lastName}`}
      </div>
      <br />
      <h4>{headline}</h4>
      <br />
      <p>
        <span>Original claim:</span>
        <i>"{claim.text}"</i>
      </p>
      <br />
      <div className="tags">
        {verdictTags.map((tag) => (
          <span className="tag text-center" key={tag.id}>
            {tag.tag.label}
          </span>
        ))}
      </div>
    </div>
  );
};

_.propTypes = {
  verdict: PropTypes.shape({
    claim: PropTypes.shape({
      text: PropTypes.string.isRequired,
    }),
    editor: PropTypes.shape({
      firstName: PropTypes.string.isRequired,
      lastName: PropTypes.string.isRequired,
    }),
    id: PropTypes.string,
    verdictTags: PropTypes.arrayOf(
      PropTypes.shape({
        tag: PropTypes.shape({
          label: PropTypes.string,
        }),
      })
    ),
  }),
};

export default _;
