export const canSubmitFromFormState = config => {
  if (!config) {
    throw new Error('getCanSubmit: Missing arguments')
  }
  const { isLoading, ...reactFinalFormProps } = config
  // https://github.com/final-form/final-form#formstate
  const {
    dirtySinceLastSubmit,
    hasSubmitErrors,
    hasValidationErrors,
    pristine,
  } = reactFinalFormProps

  const canSubmit =
    !isLoading &&
    ((!pristine && !hasSubmitErrors && !hasValidationErrors) ||
      (!hasValidationErrors && hasSubmitErrors && dirtySinceLastSubmit))

  return canSubmit
}


export const composeValidators = (...validators) => value =>
  validators.reduce(
    (error, validator) =>
      error ||
      (typeof validator === 'function' && validator(value)),
    undefined
  )


export const createParseNumberValue = type => value => {
  if (typeof value === 'undefined') {
    return null
  }

    let stringifiedNumberValue = value
    if (typeof stringifiedNumberValue !== 'string') {
        stringifiedNumberValue = String(value)
    }

    if (stringifiedNumberValue === '') {
        return ''
    }

    if (type === 'number') {
        let number
        if (stringifiedNumberValue.includes('.')) {
            number = parseFloat(stringifiedNumberValue)
        } else if (stringifiedNumberValue.includes(',')) {
            const formattedValue = stringifiedNumberValue.replace(/,/g, '.')
            number = parseFloat(formattedValue)
        } else {
            number = parseInt(stringifiedNumberValue, 10)
        }
        return number
    }

    return stringifiedNumberValue
}


export const hasMinLength = (value, min) => {
  if (!isString(value) || typeof min !== 'number') return false
  return value.length >= min
}


export const hasUppercase = value => {
  if (!isString(value) || !value.trim().length) return false
  return /[A-Z]/.test(value)
}


export const hasLowercase = value => {
  if (!isString(value) || !value.trim().length) return false
  return /[a-z]/.test(value)
}


export const hasNumber = value => {
  if (!isString(value) || !value.trim().length) return false
  return /[0-9]/.test(value)
}


export const isEmpty = value => {
  if (!isString(value)) return false
  return value.trim().length === 0
}


export const isString = value => {
  if (typeof value !== 'string') return false
  return true
}


export const isPassword = (value, count = 12) =>
  value &&
  isString(value) &&
  hasMinLength(value, count) &&
  hasUppercase(value) &&
  hasLowercase(value) &&
  hasNumber(value)


export const getRequiredValidate = required => {
  const requiredIsAFunction = required && typeof required === 'function'
  const defaultRequiredValidate =
    (required && validateRequiredField) || undefined
  const requiredValidate = requiredIsAFunction
    ? required
    : defaultRequiredValidate
  return requiredValidate
}

const createValidateRequiredField = error => value => {
  if (value && !isEmpty(value)) return undefined
  return error
}

const validateRequiredField = createValidateRequiredField('This field is obligatory')
