import React, { useCallback, useMemo } from 'react'
import { useDispatch } from 'react-redux'
import { useHistory, useLocation } from 'react-router-dom'
import { deleteData, getStateKeyFromConfig } from 'redux-thunk-data'

import { useLocationURL } from 'utils/url'

import KeywordsBar from './KeywordsBar'
import TagsSelect from './TagsSelect'


export const getItemsActivityTagFromConfig = config =>
  `/${getStateKeyFromConfig(config)}-items`


export default ({ config }) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const locationURL = useLocationURL()
  const locationSearch = locationURL.search

  const handleChange =  useCallback((key, value) => {
    const isEmptyValue = typeof value === 'undefined' || value === ''
    if (isEmptyValue) {
      locationURL.searchParams.delete(key)
    } else {
      locationURL.searchParams.set(key, value)
    }
    if (locationURL.search === search) return
    dispatch(deleteData(null, { tags: [getItemsActivityTagFromConfig(config)] }))
    setTimeout(() => history.push(*TBW*)
  }, [config, dispatch, history, locationURL, locationSearch])


  return (
    <div className="controls">
      <TagsSelect
        onChange={handleChange}
        selectedTag={locationURL.searchParams.get('tag')}
      />
      <div className="right">
        <KeywordsBar
          onChange={handleChange}
          selectedKeywords={*TBW*}
        />
      </div>
    </div>
  )
}
