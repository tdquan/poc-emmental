import { requestData } from "redux-thunk-data";
import withLogin from "with-react-redux-login";

export default withLogin({
  handleFail: (state, action, ownProps) => {
    const {
      history,
      location: { pathname, search },
    } = ownProps;
    const from = encodeURIComponent(`${pathname}${search}`);
    history.push(`/signin?from=${from}`);
  },
  isRequired: true,
  requestData,
});
