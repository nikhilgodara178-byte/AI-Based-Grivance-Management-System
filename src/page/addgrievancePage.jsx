import React from 'react'
import Navbar from "../components/navbar.jsx"
import NewGrievanceForm from '../components/newgrievanceform.jsx'
import Header from "../components/header.jsx"

const AddgrievancePage = () => {
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
          <NewGrievanceForm/>
        </div>
      </div>
    </div>
  )
}

export default AddgrievancePage