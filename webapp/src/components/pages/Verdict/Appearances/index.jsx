import React from "react";

import AppearanceItem from "./AppearanceItem";

export default ({ appearances }) => {
  if (!appearances.length) {
    return null;
  }

  return (
    <div className="appearances">
      {appearances.map((appearance) => (
        <AppearanceItem appearance={appearance} key={appearance.id} />
      ))}
    </div>
  );
};
