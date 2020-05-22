import classnames from 'classnames'
import PropTypes from 'prop-types'
import React from 'react'


const _ = ({ children, className, Tag }) => (
  <Tag className={classnames('main', className)}>
    {children}
  </Tag>
)


_.defaultProps = {
  className: null,
  Tag: 'main',
}


_.propTypes = {
  Tag: PropTypes.string,
  children: PropTypes.node.isRequired,
  className: PropTypes.string,
}


export default _
