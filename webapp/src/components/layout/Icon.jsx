import PropTypes from 'prop-types'
import React from 'react'

import { ROOT_ASSETS_PATH } from 'utils/config'


const _ = ({ name, path, ...imgProps }) => (
  <img
    {...imgProps}
    alt={name}
    className={imgProps.className || 'icon'}
    src={`${path}/${name}`}
  />
)

_.defaultProps = {
  path: ROOT_ASSETS_PATH
}

_.propTypes = {
  name: PropTypes.string.isRequired,
  path: PropTypes.string
}

export default _
