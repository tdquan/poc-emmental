import classnames from 'classnames'
import PropTypes from 'prop-types'
import React, { useCallback } from 'react'
import { useHistory } from 'react-router-dom'


const _ = ({ className, verdict }) => {
  const {
    claim,
    editor,
    id,
    verdictTags,
    title: headline
  } = verdict
  const { quotedFromAppearances } = claim || {}


  const history = useHistory()

  const handleClick = useCallback(() =>
    history.push(*TBW*), [history, id])


  return (
    <div
      className={classnames('verdict-item', className)}
      onClick={handleClick}
    >
      *TBW*
    </div>
  )
}


_.propTypes = {
  verdict: PropTypes.shape({
    claim: PropTypes.shape({
      text: PropTypes.string.isRequired
    }),
    editor: PropTypes.shape({
      firstName: PropTypes.string.isRequired,
      lastName: PropTypes.string.isRequired
    }),
    id: PropTypes.string,
    verdictTags: PropTypes.arrayOf(PropTypes.shape({
      tag: PropTypes.shape({
        label: PropTypes.string
      })
    }))
  })
}


export default _
