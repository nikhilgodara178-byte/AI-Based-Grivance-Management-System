import React from 'react'
import AdminDashboard from '../components/admin_dashboard'
import Navbar from '../components/navbar'
import Header from '../components/header'

const AdminDashboardepage = () => {
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
                    <AdminDashboard />
                </div>
            </div>
        </div>
    )
}

export default AdminDashboardepage