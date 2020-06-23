/* eslint
  react/jsx-one-expression-per-line: 0 */
import classnames from 'classnames'
import PropTypes from 'prop-types'
import React, { useCallback } from 'react'
import { Field } from 'react-final-form'

import {
  composeValidators,
  createParseNumberValue,
  getRequiredValidate
} from 'utils/form'

import FieldError from '../FieldError'


const _ = ({
  autoComplete,
  disabled,
  id,
  label,
  name,
  placeholder,
  readOnly,
  renderInner,
  renderValue,
  required,
  sublabel,
  type,
  validate,
}) => {

  const renderField = useCallback(({ input, meta }) => (
    <div
      className={classnames(`${type}-field`, { readonly: readOnly })}
      id={id}
    >
      <label
        className="field-label"
        htmlFor={name}
      >
        <span>{label}</span>
        {required && !readOnly && <span className="field-asterisk">{"*"}</span>}
      </label>
      {sublabel && (
        <label
          className="field-sublabel"
          htmlFor={name}
        >
          <span>{sublabel}</span>
        </label>
      )}
      <div className="field-control">
        <div className="field-value">
          <div className="field-inner">
            <input
              {...input}
              autoComplete={autoComplete ? 'on' : 'off'}
              className="field-input"
              disabled={disabled || readOnly}
              name={name}
              placeholder={readOnly ? '' : placeholder}
              readOnly={readOnly}
              required={!!required}
              type={type}
            />
            {renderInner()}
          </div>
          {renderValue()}
        </div>
        <FieldError meta={meta} />
      </div>
    </div>
  ), [autoComplete, disabled, id, label, name, placeholder, readOnly, renderInner, renderValue, required, sublabel, type])

  return (
    <Field
      name={name}
      parse={createParseNumberValue(type)}
      render={renderField}
      validate={composeValidators(validate, getRequiredValidate(required))}
    />
  )
}


_.defaultProps = {
  autoComplete: false,
  disabled: false,
  id: null,
  placeholder: 'Please enter a value',
  readOnly: false,
  renderInner: () => null,
  renderValue: () => null,
  required: false,
  sublabel: null,
  type: 'text',
  validate: null,
}

_.propTypes = {
  autoComplete: PropTypes.bool,
  disabled: PropTypes.bool,
  id: PropTypes.string,
  label: PropTypes.string.isRequired,
  name: PropTypes.string.isRequired,
  placeholder: PropTypes.string,
  readOnly: PropTypes.bool,
  renderInner: PropTypes.func,
  renderValue: PropTypes.func,
  required: PropTypes.oneOfType([PropTypes.bool, PropTypes.func]),
  sublabel: PropTypes.string,
  type: PropTypes.string,
  validate: PropTypes.func,
}

export default _
