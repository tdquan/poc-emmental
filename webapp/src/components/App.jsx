import PropTypes from "prop-types";
import React, { Fragment } from "react";
import Helmet from "react-helmet";

const _ = ({ children }) => (
  <Fragment>
    <Helmet>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta name="apple-mobile-web-app-capable" content="yes" />
      <meta name="mobile-web-app-capable" content="yes" />
      <meta name="theme-color" content="#ffffff" />
      <meta
        httpEquiv="Content-Security-Policy"
        content="default-src 'self' blob: data: https: http: gap://ready 'unsafe-inline'
                'unsafe-eval';
                style-src 'self' 'unsafe-inline';
                connect-src 'self' https: http: ws://localhost:3000 wss://web-local:3000"
      />
      <title>Poc Webapp</title>
    </Helmet>
    {children}
  </Fragment>
);

_.propTypes = {
  children: PropTypes.node.isRequired,
};

export default _;
