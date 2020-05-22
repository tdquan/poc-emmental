import { combineReducers } from 'redux'
import { modals } from 'redux-react-modals'
import { createDataReducer, createRequestsReducer } from 'redux-thunk-data'


export const data = createDataReducer()
export const requests = createRequestsReducer()

export default combineReducers({
  data,
  modals,
  requests
})
