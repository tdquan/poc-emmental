import React from "react";

export default ({ appearance }) => {
  const { quotingContent } = appearance;
  const { url } = quotingContent || {};

  const source = quotingContent?.medium?.name
    ? quotingContent.medium.name
    : new URL(url).host;

  return (
    <div className="appearance-item">
      <span>{source}</span>
      <span>
        <a href={url} target="_blank" rel="noopener noreferrer">
          [link]
        </a>
      </span>
    </div>
  );
};
