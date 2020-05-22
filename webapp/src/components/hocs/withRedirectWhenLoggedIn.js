import { requestData } from 'redux-thunk-data'
import withLogin from 'with-react-redux-login'


export default withLogin({
  handleSuccess: (state, action, ownProps) => {
    const { history } = ownProps
    history.push('/')
  },
  isRequired: false,
  requestData,
})
