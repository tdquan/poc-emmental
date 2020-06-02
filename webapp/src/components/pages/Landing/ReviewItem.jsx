import PropTypes from "prop-types";
import React from "react";

const _ = ({ review }) => {
  const { claim, reviewer } = review;

  return (
    <div className="review-item">
      <div className="claim">"{claim.text}"</div>
      <div className="reviewer">
        reviewed by {`${reviewer.firstName} ${reviewer.lastName}`}
      </div>
    </div>
  );
};

_.propTypes = {
  review: PropTypes.object.isRequired,
};

export default _;
