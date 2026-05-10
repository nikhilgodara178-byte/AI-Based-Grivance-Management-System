import React from 'react'
import Profile from '../components/profilecompt'
import Navbar from '../components/navbar'
import Header from '../components/header'

const Profilepage = () => {
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
                    <Profile />
                </div>
            </div>
        </div>
    )
}

export default Profilepage