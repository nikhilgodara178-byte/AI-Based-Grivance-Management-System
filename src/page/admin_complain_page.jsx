import React from 'react'
import AdminComplain from '../components/admin_complain'
import Navbar from '../components/navbar'
import Header from '../components/header'

const AdminComplainPage = () => {
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
                    <AdminComplain />
                </div>
            </div>
        </div>
    )
}

export default AdminComplainPage