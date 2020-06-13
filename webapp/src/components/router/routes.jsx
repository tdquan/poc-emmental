import Landing from "components/pages/Landing";
import Verdict from "components/pages/Verdict";
import Verdicts from "components/pages/Verdicts";

export default [
  {
    component: Landing,
    exact: true,
    path: "/",
    title: "Landing",
  },
  {
    component: Verdict,
    exact: true,
    path: "/verdicts/:verdictId([A-Za-z0-9]{2,})",
    title: "Verdict",
  },
  {
    component: Verdicts,
    exact: true,
    path: "/verdicts",
    title: "Verdicts",
  },
];
