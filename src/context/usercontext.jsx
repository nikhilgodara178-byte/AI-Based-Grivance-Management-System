import { createContext, useState, useEffect } from "react";

export const userContext = createContext({});

export const UserContextProvider = ({ children }) => {
    const [User, setUser] = useState({});

    useEffect(() => {
        if (User.u_id) {
            console.log("add user to local storage", User)
            localStorage.setItem("user", JSON.stringify(User));
        } else {
            const user = localStorage.getItem("user")
            if (user) {
                console.log("get user from local storage: ", user)
                setUser(JSON.parse(user))
            }
        }
    }, [User]);

    const logout = () => {
        setUser([]);
        localStorage.removeItem("user");
    };

    return (
        <userContext.Provider value={{ User, setUser, logout }}>
            {children}
        </userContext.Provider>
    );
};
