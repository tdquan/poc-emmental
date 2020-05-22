import classnames from 'classnames'
import PropTypes from 'prop-types'
import React from 'react'
import { Modal } from 'redux-react-modals'


const _ = ({ children, className, Tag }) => (
  <Tag className={classnames('main', className)}>
    <Modal name="main" />
    {children}
  </Tag>
)


_.defaultProps = {
  Tag: 'main',
  className: null
}


_.propTypes = {
  Tag: PropTypes.string,
  children: PropTypes.node.isRequired,
  className: PropTypes.string,
}


export default _
