import React from "react";

import TextField from "components/layout/form/fields/TextField";
import PasswordField from "components/layout/form/fields/PasswordField";

export default () => {
  return (
    <>
      <TextField
        id="identifier"
        name="identifier"
        label="email"
        required
        placeholder="Your login"
        type="email"
      />
      <PasswordField
        id="password"
        name="password"
        label="password"
        required
        placeholder="Your login password"
      />
    </>
  );
};
