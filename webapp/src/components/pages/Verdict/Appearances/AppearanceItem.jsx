import React from 'react'


export default ({ appearance }) => {
  const { quotingContent } = appearance
  const { url } = quotingContent || {}

  return (
    <div className="appearance-item">
      *TBW*
    </div>
  )
}
