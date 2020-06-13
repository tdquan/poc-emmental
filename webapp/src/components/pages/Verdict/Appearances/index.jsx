import React from "react";

import AppearanceItem from "./AppearanceItem";

export default ({ appearances }) => {
  if (!appearances.length) {
    return null;
  }

  return <div className="appearances">*TBW*</div>;
};
