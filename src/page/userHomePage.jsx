import React from 'react'
import Navbar from '../components/navbar'
import Header from '../components/header'
import Grienvancelist from '../components/grienvancelist'
import "../css/userhomepage.css"

const UserHomePage = () => {
  return (
    <div className='home-page-cont'>
      <div className='nav-cont'>
        <Navbar />
      </div>
      <div className='header-list-cont'>
        <div>
          <Header />
        </div>
        <div>
          <Grienvancelist />
        </div>
      </div>
    </div>
  )
}

export default UserHomePage