import React, { useContext } from 'react';
import "../css/navbar.css";
import PersonIcon from '@mui/icons-material/Person';
import DashboardIcon from '@mui/icons-material/Dashboard';
import ReportIcon from '@mui/icons-material/Report';
import SettingsIcon from '@mui/icons-material/Settings';
import HelpIcon from '@mui/icons-material/Help';
import LogoutIcon from '@mui/icons-material/Logout';
import { NavLink } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { userContext } from '../context/usercontext';
import { Avatar } from "@mui/material"

const Navbar = () => {
  const navigate = useNavigate()
  const { User, logout } = useContext(userContext)

  return (
    <div className="sidebar">
      <div className="brand">
        {User.full_name ? (
          <>
            <div>
              <Avatar
                sx={{
                  width: 50,
                  height: 50,
                  mx: 'auto',
                  mb: 2,
                  bgcolor: 'primary.main',
                }}>
                {User.full_name.split("")[0][0]}
              </Avatar>
            </div>
            <div className="brand-text">
              <h3>{User.full_name}</h3>
              <p>{User.department}</p>
            </div>
          </>
        ) : (
          <>
            <div className="button-cont-nav">
              <div className="login-btn" onClick={() => navigate("/login")}>Login</div>
              <div className="signup-btn" onClick={() => navigate("/signup")}>Sign Up</div>
            </div>
          </>
        )}

      </div>

      <ul className="nav-links">
        <NavLink to={"/dashboard"} className={({ isActive }) => (isActive ? 'active' : '')}><li><DashboardIcon sx={{ height: "70%", width: 'auto' }} /><span>Dashboard</span></li></NavLink>

        <NavLink to={"/"} className={({ isActive }) => (isActive ? 'active' : '')}><li><ReportIcon sx={{ height: "70%", width: 'auto' }} /><span>Complaints</span></li></NavLink>

        <NavLink to={"/profile"} className={({ isActive }) => (isActive ? 'active' : '')}><li><PersonIcon sx={{ height: "70%", width: 'auto' }} /><span>Profile</span></li></NavLink>

        <NavLink to={"/settings"} className={({ isActive }) => (isActive ? 'active' : '')}><li><SettingsIcon sx={{ height: "70%", width: 'auto' }} /><span>Settings</span></li></NavLink>

      </ul>

      <div className="logout" onClick={logout}>
        <LogoutIcon /><span>Logout</span>
      </div>
    </div>
  );
};

export default Navbar;
