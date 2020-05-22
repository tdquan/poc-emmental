import React from 'react'
import { useSelector } from 'react-redux'
import { NavLink, useLocation } from 'react-router-dom'
import { selectCurrentUser } from 'with-react-redux-login'

import Icon from 'components/layout/Icon'

import Signout from './Signout'


export default () => {
  const { pathname } = useLocation()
  const currentUser = useSelector(selectCurrentUser)
  const showToSignin = typeof currentUser === 'undefined' &&
                       pathname !== '/signin'


  return (
    <div className="header">
      <NavLink to="/">
        <Icon name="logo.svg" />
      </NavLink>
      {showToSignin && (
        *TBW*
      )}
      {currentUser && (
          <Signout>
            {'Sign out'}
          </Signout>
        )}
    </div>
  )
}
