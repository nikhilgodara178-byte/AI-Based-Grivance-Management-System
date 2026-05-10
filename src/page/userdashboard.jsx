import React from 'react'
import Navbar from '../components/navbar'
import Header from '../components/header'
import Dashboard from '../components/dashboard'

const Userdashboard = () => {
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
                    <Dashboard />
                </div>
            </div>
        </div>
    )
}

export default Userdashboard