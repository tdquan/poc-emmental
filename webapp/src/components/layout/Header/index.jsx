import React from "react";
import { useSelector } from "react-redux";
import { NavLink, useLocation, useHistory } from "react-router-dom";
import { selectCurrentUser } from "with-react-redux-login";

import Icon from "components/layout/Icon";

import Signout from "./Signout";

export default () => {
  const { pathname } = useLocation();
  const currentUser = useSelector(selectCurrentUser);
  const history = useHistory();
  const showToSignin =
    typeof currentUser === "undefined" && pathname !== "/signin";

  const handleSignin = () => history.push("/signin");

  console.log(currentUser);

  return (
    <div className="header">
      <NavLink to="/">
        <Icon name="logo.svg" />
      </NavLink>
      {showToSignin && (
        <button className="signin" onClick={handleSignin}>
          Sign in
        </button>
      )}
      {currentUser && <Signout>Sign out</Signout>}
    </div>
  );
};
