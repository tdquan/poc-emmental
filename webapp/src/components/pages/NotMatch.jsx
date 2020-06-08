import React, { useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { Redirect } from 'react-router-dom'


const _ = ({ delay, location, redirect }) => {
 const [timing, setTiming] = useState(delay)


 useEffect(() => {
   const timeout = 1000
   const timer = setInterval(() => {
     setTiming(({ timing }) => ({ timing: timing - 1 }))
   }, timeout)

   return () => {
     clearInterval(timer)
   }
 }, [setTiming])


 if (timing < 0) return <Redirect to={redirect} />


 return (
   <div className="not-match">
     <h3 className="title">
       {`404 Not found ${location.pathname}`}
     </h3>
     <p className="content">
       {timing > 0 && (
         (
           <span>
             {`You are going to be redirected in ${timing} seconds`}
           </span>
         )
       )}
       {timing === 0 && (
         <span>
           {'Redirecting...'}
         </span>
       )}
     </p>
   </div>
 )
}

_.defaultProps = {
 delay: 5,
 redirect: '/',
}

_.propTypes = {
 delay: PropTypes.number,
 location: PropTypes.object.isRequired,
 redirect: PropTypes.string,
}

export default _
