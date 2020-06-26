import PropTypes from "prop-types";
import React, { useCallback } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { closeModal } from "redux-react-modals";
import { reinitializeData, requestData } from "redux-thunk-data";

const _ = ({ children }) => {
  const dispatch = useDispatch();
  const history = useHistory();

  const handleSignoutClick = useCallback(() => {
    dispatch(
      requestData({
        apiPath: "/users/signout",
        handleSuccess: () => {
          history.push("/signin");
          dispatch(reinitializeData());
        },
        name: "signout",
        stateKey: null,
      })
    );
    dispatch(closeModal("main"));
  }, [dispatch, history]);

  return (
    <button className="signout" onClick={handleSignoutClick}>
      {children}
    </button>
  );
};

_.defaultProps = {
  children: null,
};

_.propTypes = {
  children: PropTypes.node,
};

export default _;
