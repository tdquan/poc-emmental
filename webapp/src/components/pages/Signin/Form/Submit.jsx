import classnames from 'classnames'
import React from 'react'
import { useSelector } from 'react-redux'


export default () => {
  const { isPending } = useSelector(state =>
    state.requests['/users/signin']) || {}


  return (
    <button
      className={classnames('submit', {
        'is-loading': isPending,
      })}
      disabled={isPending}
      type="submit"
    >
        Sign in
    </button>
  )
}
