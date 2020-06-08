import PropTypes from 'prop-types'
import React from 'react'
import Helmet from 'react-helmet'


const _ = ({ children }) => (
  <>
    <Helmet>
      <meta charset="utf-8" />
      <meta name="viewport" content=*TBW* />
      <meta name="apple-mobile-web-app-capable" content="yes" />
      <meta name="mobile-web-app-capable" content="yes" />
      <meta name="theme-color" content="#ffffff" />
      <meta
        httpEquiv="Content-Security-Policy"
        content=*TBW*
      />
      <title>Poc Webapp</title>
    </Helmet>
    {children}
  </>
)


_.propTypes = {
  children: PropTypes.node.isRequired,
}


export default _
