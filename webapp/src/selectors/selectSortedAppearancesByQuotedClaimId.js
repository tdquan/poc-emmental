import createCachedSelector from "re-reselect";
import { selectEntitiesByKeyAndJoin } from "redux-thunk-data";
import { selectCurrentUser } from "with-react-redux-login";

const mapArgsToCacheKey = (state, claimId) => claimId || "";

export default createCachedSelector(
  selectCurrentUser,
  (state, claimId) =>
    selectEntitiesByKeyAndJoin(state, "appearances", {
      key: "quotedClaimId",
      value: claimId,
    }),
  (currentUser, appearances) => {
    if (!appearances) return;
    appearances.sort();
    if (currentUser) {
      appearances.sort();
    }
    return appearances;
  }
)(mapArgsToCacheKey);
