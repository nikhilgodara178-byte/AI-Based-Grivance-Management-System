import React from 'react'
import AdminProfileSettings from '../components/admin_profile_setting'
import Navbar from '../components/navbar'
import Header from '../components/header'

const Adminprofile = () => {
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
                    <AdminProfileSettings />
                </div>
            </div>
        </div>
    )
}

export default Adminprofile