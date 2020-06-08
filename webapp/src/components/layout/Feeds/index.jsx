import React from "react";

import Controls from "./Controls";
import Items from "./Items";

export default ({ config, renderItem }) => (
  <>
    <Controls config={config} />
    <Items config={config} renderItem={renderItem} />
  </>
);
