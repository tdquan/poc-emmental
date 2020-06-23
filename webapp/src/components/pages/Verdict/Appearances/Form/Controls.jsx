import classnames from 'classnames'
import React, { useCallback } from 'react'
import { useForm } from 'react-final-form'
import { useDispatch, useSelector } from 'react-redux'
import { useHistory, useParams } from 'react-router-dom'
import { closeModal } from 'redux-react-modals'

import { canSubmitFromFormState } from 'utils/form'


export default props => {
  const dispatch = useDispatch()
  const { getState, } = useForm()
  const history = useHistory()
  const { verdictId } = useParams()

  const { isPending } = useSelector(state =>
    state.requests['/appearances']) || {}

  const canSubmit = canSubmitFromFormState({ isLoading: isPending, ...getState() })


  const handleCancel = useCallback(() => {
    history.push(`/verdicts/${verdictId}/appearances`)
    dispatch(*TBW*)
  }, [dispatch, history, verdictId])


  return (
    <div className="controls">
      <button
        className={classnames({
          'is-disabled': !canSubmit,
          'is-loading': isPending,
        })}
        disabled={!canSubmit}
        type=*TBW*
      >
        Submit
      </button>
      <button
        className="cancel"
        onClick={*TBW*}
      >
        Cancel
      </button>
    </div>
  )
}
