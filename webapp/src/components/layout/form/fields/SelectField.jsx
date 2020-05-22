import classnames from 'classnames'
import PropTypes from 'prop-types'
import React, { useMemo } from 'react'
import { Field } from 'react-final-form'

import {
  composeValidators,
  getRequiredValidate
} from 'utils/form'

import FieldError from '../FieldError'


const _ = ({
  className,
  disabled,
  label,
  name,
  options,
  placeholder,
  readOnly,
  required,
  validate
}) => {
  const optionsWithPlaceholder = useMemo(() =>
    [{ label: placeholder, value: '' }].concat(options), [options, placeholder])


  return (
    <Field
      name={name}
      validate={composeValidators(validate, getRequiredValidate(required))}
      render={({ input, meta }) => (
        <div className={classnames('select-field', { readonly: readOnly })}>
          <label htmlFor={name} className={classnames('field-label', { empty: !label })}>
            {label && (
              <span>
                <span>{label}</span>
                {required && !readOnly && <span className="field-asterisk">*</span>}
              </span>
            )}
          </label>
          <div className="field-control">
            <div className="field-value">
              <div className="field-inner">
                <select
                  {...input}
                  disabled={disabled || readOnly}
                  id={name}
                  placeholder={placeholder}
                  readOnly={readOnly}
                  required={!!required}
                >
                  {optionsWithPlaceholder.map((option, index) => (
                    <option
                      disabled={index === 0}
                      id={option.value}
                      key={option.value}
                      value={option.value}
                    >
                      {option.label}
                    </option>
                  ))}
                </select>
              </div>
            </div>
          </div>
          <FieldError meta={meta} />
        </div>
      )}
    />
  )
}

_.defaultProps = {
  className: '',
  disabled: false,
  label: '',
  optionLabelKey: 'label',
  optionValueKey: 'id',
  options: null,
  placeholder: 'Please select a value',
  readOnly: false,
  required: false,
  validate: null,
  validating: false
}

_.propTypes = {
  className: PropTypes.string,
  disabled: PropTypes.bool,
  label: PropTypes.string,
  name: PropTypes.string.isRequired,
  optionLabelKey: PropTypes.string,
  optionValueKey: PropTypes.string,
  options: PropTypes.array,
  placeholder: PropTypes.string,
  readOnly: PropTypes.bool,
  required: PropTypes.oneOfType([PropTypes.bool, PropTypes.func]),
  validate: PropTypes.func,
  validating: PropTypes.bool,
}

export default _
