import React from "react";

export default ({ appearance }) => {
  const { quotingContent } = appearance;
  const { url } = quotingContent || {};

  const source = quotingContent?.medium?.name
    ? quotingContent.medium.name
    : new URL(url).host;

  return (
    <div className="appearance-item">
      <h3>
        <u>Appears in:</u>
      </h3>
      <div>{source}</div>
      <div>
        <a href={url} target="_blank">
          [link]
        </a>
      </div>
    </div>
  );
};
