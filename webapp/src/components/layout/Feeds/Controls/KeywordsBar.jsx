import PropTypes from 'prop-types'
import React, { useCallback, useEffect, useRef, useState } from 'react'


import Icon from 'components/layout/Icon'


const _ = ({
  onChange,
  selectedKeywords
}) => {
  const inputRef = useRef()


  const [value, setValue] = useState(selectedKeywords)


  const handleKeywordsClick = useCallback(() =>
    onChange('keywords', value), [onChange, value])

  const handlePressEnter = useCallback(event => {
    if (event.keyCode === 13) {
      event.preventDefault()
      handleKeywordsClick()
    }
  }, [handleKeywordsClick])


  useEffect(() => {
    const inputElement = inputRef.current
    inputElement.addEventListener("keyup", handlePressEnter)
    return () => inputElement.removeEventListener("keyup", handlePressEnter)
  }, [handlePressEnter])


  return (
    <div className="keywords-bar">
      <input
        className="keywords-input"
        defaultValue={value}
        name="keywords"
        onChange={event => setValue(event.target.value)}
        placeholder="Type your search"
        ref={inputRef}
      />
      <button
        className="is-inner-input"
        onClick={handleKeywordsClick}
        type="button"
      >
        <Icon className="icon" name="loupe.svg" />
      </button>
    </div>
  )
}


_.propTypes = {
  onChange: PropTypes.func.isRequired,
  selectedKeywords: PropTypes.string
}

export default _
