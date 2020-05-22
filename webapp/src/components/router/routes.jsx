import withRedirectWhenLoggedIn from 'components/hocs/withRedirectWhenLoggedIn'
import withRequiredLogin from 'components/hocs/withRequiredLogin'
import Landing from 'components/pages/Landing'
import Signin from 'components/pages/Signin'
import Verdict from 'components/pages/Verdict'
import Verdicts from 'components/pages/Verdicts'


export default [
  {
    component: Landing,
    exact: true,
    path: '/',
    title: 'Landing',
  },
  {
    component: withRedirectWhenLoggedIn(Signin),
    exact: true,
    path: '/signin',
    title: 'Signin'
  },
  {
    component: withRequiredLogin(Verdict),
    exact: true,
    path: '/verdicts/:verdictId([A-Za-z0-9]{2,})/appearances/:appearanceId(creation)?',
    title: 'Verdict Create Appearance',
  },
  {
    component: *TBW*,
    exact: true,
    path: '/verdicts/:verdictId([A-Za-z0-9]{2,})',
    title: *TBW*,
  },
  {
    component: Verdicts,
    exact: true,
    path: *TBW*,
    title: *TBW*,
  }
]
