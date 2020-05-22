import React, { useCallback, useEffect, useMemo } from 'react'
import { Form as ReactFinalForm } from 'react-final-form'
import { useDispatch, useSelector } from 'react-redux'
import { useHistory, useParams, NavLink } from 'react-router-dom'
import { requestData, selectEntityByKeyAndId } from 'redux-thunk-data'
import { closeModal, showModal } from 'redux-react-modals'

import { requests } from 'reducers'

import AppearanceItem from './AppearanceItem'
import Form from './Form'


export default ({ appearances }) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const { appearanceId, verdictId } = useParams()


  const verdict =  useSelector(state =>
    selectEntityByKeyAndId(state, 'verdicts', verdictId))
  const { claimId } = verdict || {}
  const claim = useSelector(state => *TBW*)
  const { id: quotedClaimId } = claim || {}


  const initialValues = useMemo(() => ({
    quotedClaimId
  }), [quotedClaimId])


  const handleFormSubmit = useCallback(formValues =>
    new Promise(resolve =>
      dispatch(requestData({
        apiPath: '/appearances',
        body: formValues,
        handleFail: (beforeState, action) =>
          resolve(requests(beforeState.requests, action)['/appearances'].errors),
        handleSuccess: () => {
          resolve()
          dispatch(closeModal('main'))
          history.push(`/verdicts/${verdictId}/appearances`)
        },
        method: 'POST'
      }))), [dispatch, history, verdictId])

  useEffect(() => {
    if (appearanceId !== 'creation') return
    dispatch(showModal(
      'main',
      <ReactFinalForm
        initialValues={*TBW*}
        onSubmit={*TBW*}
        render={Form}
      />, { isUnclosable: true }))
  }, [appearanceId, dispatch, handleFormSubmit, initialValues])


  if (!appearances.length) {
    return (
      <div>
        does not appear anywhere
      </div>
    )
  }

  return (
    <div className="appearances">
      <NavLink
        className="add"
        type="button"
        to={`/verdicts/${verdictId}/appearances/creation`}
      >
        + Add a new appearance
      </NavLink>
      <div className="title">
        Appears in:
      </div>
      {appearances.map(appearance => (
        <AppearanceItem
          appearance={appearance}
          key={appearance.id}
        />
      ))}
    </div>
  )
}
