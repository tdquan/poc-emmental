/* eslint
  react/jsx-one-expression-per-line: 0 */
import PropTypes from 'prop-types'
import React from 'react'


const setDangerousArrayKeyIndex = index => `field_error_${index}`


export const _ = ({ className, customMessage, meta }) => {
  const showError =
    customMessage ||
    (meta &&
      meta.touched &&
      (meta.error || (!meta.dirtySinceLastSubmit && meta.submitError)))
  let errorMessage =
    (showError &&
      (customMessage ||
        (meta.error || (!meta.dirtySinceLastSubmit && meta.submitError)))) ||
    null
  errorMessage = !errorMessage
    ? null
    : (Array.isArray(errorMessage) && errorMessage) || [].concat(errorMessage)


  return (
    <span className={`field-error ${className}`}>
      {(errorMessage && (
        <span className="icon-and-messages">
          <span className="icon">
            <span
              aria-hidden
              className="icon-warning-circled"
              title=""
            />
          </span>
          <span className="messages">
            {errorMessage.map((err, index) => (
              <span
                key={setDangerousArrayKeyIndex(index)}
                className="message"
              >
                {err}
              </span>
            ))}
          </span>
        </span>
      )) ||
        null}
    </span>
  )
}

_.defaultProps = {
  className: '',
  customMessage: '',
  meta: null,
}

_.propTypes = {
  className: PropTypes.string,
  customMessage: PropTypes.string,
  meta: PropTypes.object,
}

export default _
