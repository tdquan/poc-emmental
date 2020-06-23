import React from "react";
import { Provider } from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import NotMatch from "components/pages/NotMatch";
import routes from "components/router/routes";
import configureStore from "utils/store";

import App from "./App";

const { store } = configureStore();

export default () => (
  <Provider store={store}>
    <BrowserRouter>
      <App>
        <Switch>
          {routes.map((route) => (
            <Route
              exact
              path={route.path}
              component={route.component}
              key={route.path}
            />
          ))}
          <Route component={NotMatch} />
        </Switch>
      </App>
    </BrowserRouter>
  </Provider>
);
