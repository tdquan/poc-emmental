import React from 'react'
import { useSelector } from 'react-redux'

import Fields from './Fields'
import Submit from './Submit'


export default ({ handleSubmit }) => {
  const { isPending } = useSelector(state =>
    state.requests['/users/signin']) || {}

  return (
    <form
      autoComplete="off"
      disabled={isPending}
      noValidate
      onSubmit={handleSubmit}
    >
      <Fields />
      <Submit />
    </form>
  )
}
