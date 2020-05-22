import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { requestData } from 'redux-thunk-data'

import Header from 'components/layout/Header'
import Main from 'components/layout/Main'

import ReviewItem from './ReviewItem'


const KEYWORDS_CHAIN = 'coronavirus'


export default () => {
  const dispatch = useDispatch()

  const reviews = useSelector(state => *TBW*)


  useEffect(() => {
    const apiPath = `/reviews?keywords=${KEYWORDS_CHAIN}`
    dispatch(requestData({ apiPath }))
  }, [dispatch])


  return (
    <>
      <Header />
      <Main className="landing">
        <div className="container">
          <section className="title">
            {`Reviews for "${KEYWORDS_CHAIN}": `}
          </section>
          <section className="results">
            {(reviews || []).map(*TBW*)}
          </section>
        </div>
      </Main>
    </>
  )
}
