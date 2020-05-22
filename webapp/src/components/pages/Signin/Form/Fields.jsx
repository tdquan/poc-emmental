import React from 'react'

import TextField from 'components/layout/form/fields/TextField'
import PasswordField from 'components/layout/form/fields/PasswordField'


export default () => {
  return (
    <>
      <TextField
        *TBW*
      />
      <PasswordField
        id="password"
        name="password"
        label="password"
        required
        placeholder="Your login password"
      />
    </>
  )
}
