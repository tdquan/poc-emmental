import { combineReducers } from 'redux'
import { createDataReducer } from 'redux-thunk-data'


export default combineReducers({
  data: createDataReducer()
})
