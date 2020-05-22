import React, { useCallback } from 'react'
import { Form as ReactFinalForm } from 'react-final-form'
import { useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import { requestData } from 'redux-thunk-data'
import { resolveCurrentUser } from 'with-react-redux-login'

import Header from 'components/layout/Header'
import Main from 'components/layout/Main'
import { requests } from 'reducers'
import { useLocationURL } from 'utils/url'

import Form from './Form'


export default () => {
  const dispatch = useDispatch()
  const history = useHistory()
  const locationURL = useLocationURL()
  const from = locationURL.searchParams.get('from')


  const handleFormSubmit = useCallback(formValues =>
    new Promise(resolve => {
      dispatch(requestData({
        apiPath: *TBW*,
        body: formValues,
        handleFail: (beforeState, action) =>
          resolve(requests(beforeState.requests, action)['/users/signin'].errors),
        handleSuccess: (state, action) => {
          resolve()
          const nextUrl = from
            ? decodeURIComponent(from)
            : '/'
          history.push(nextUrl)
        },
        method: 'POST',
        resolve: resolveCurrentUser
      }))
    }), [dispatch, from, history])


  return (
    <>
      <Header />
      <Main
        className="signin"
        withHeader
      >
        <section>
          <ReactFinalForm
            onSubmit={handleFormSubmit}
            render={Form}
          />
        </section>
      </Main>
    </>
  )
}
