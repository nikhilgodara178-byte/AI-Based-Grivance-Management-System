import React from 'react'
import Settings from '../components/setting'
import Navbar from '../components/navbar'
import Header from '../components/header'

const SettingsPage = () => {
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
                    <Settings />
                </div>
            </div>
        </div>
    )
}

export default SettingsPage