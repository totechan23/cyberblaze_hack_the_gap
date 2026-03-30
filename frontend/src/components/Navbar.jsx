import React from "react";
import { useNavigate } from "react-router-dom";

function Navbar({ title }) {
  const navigate = useNavigate();

  return (
    <div className="nav">
      <h2>{title}</h2>
      <button onClick={() => navigate("/")}>Logout</button>
    </div>
  );
}

export default Navbar;
