import React, { useCallback, useState } from 'react'

import Icon from 'components/layout/Icon'
import { isPassword } from 'utils/form'

import TextField from './TextField'


const createValidatePasswordField = error => value => {
  if (isPassword(value)) return undefined
  return error
}
const DEFAULT_ERROR_MESSAGE =
  'Password should contain at least 12 characters, one number, one capital letter, one lower case and one from any of _-&?~#|^@=+.$,<>%*!:;'
const validatePasswordField = createValidatePasswordField(DEFAULT_ERROR_MESSAGE)


export default props => {
  const [hidden, setHidden] = useState(true)
  const status = hidden ? '' : '-close'

  const handleToggleVisibility = useCallback(() => {
    setHidden(!hidden)
  }, [hidden, setHidden])

  const renderInner = useCallback(() => (
    <button
      className="mask"
      onClick={handleToggleVisibility}
      type="button"
    >
      <Icon name={`ico-eye${status}.svg`} />
    </button>
  ), [handleToggleVisibility, status])

  return (
    <TextField
      {...props}
      renderInner={renderInner}
      type={hidden ? 'password' : 'text'}
      validate={validatePasswordField}
    />
  )
}
