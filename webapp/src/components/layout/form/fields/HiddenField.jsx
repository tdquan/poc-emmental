import React from 'react'
import PropTypes from 'prop-types'
import { Field } from 'react-final-form'

import FieldError from '../FieldError'


const noop = () => {}


const _ = ({ name, validator }) => (
  <Field
    name={name}
    validate={validator}
    render={({ input, meta }) => (
      <>
        <input type="hidden" {...input} />
        <FieldError meta={meta} />
      </>
    )}
  />
)

_.defaultProps = {
  validator: noop,
}

_.propTypes = {
  name: PropTypes.string.isRequired,
  validator: PropTypes.func,
}

export default _
