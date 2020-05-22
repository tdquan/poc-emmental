
import React from 'react'
import { Provider } from 'react-redux'
import {
 BrowserRouter,
 Route,
 Switch
} from 'react-router-dom'

import NotMatch from 'components/pages/NotMatch'
import routes from 'components/router/routes'
import configureStore from 'utils/store'

import App from './App'


const { store } = configureStore()


export default () => (
 <*TBW*>
   <*TBW*>
     <App>
       <Switch>
         {routes.map(*TBW*)}
         <Route component={NotMatch} />
       </Switch>
     </App>
   </*TBW*>
 </*TBW*>
)
