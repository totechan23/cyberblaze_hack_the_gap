// frontend/src/pages/Login.jsx

import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api";

function Login() {
  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("citizen");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    try {
      const res = await login({ username, password, role });

      if (res.role === "citizen") {
        navigate("/citizen");
      } else if (res.role === "employee") {
        navigate("/employee");
      } else {
        setError("Invalid role");
      }
    } catch (err) {
      setError("Login failed");
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.box}>
        <h2>AI Civic Assistant</h2>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          style={styles.input}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          style={styles.input}
        />

        <select
          value={role}
          onChange={(e) => setRole(e.target.value)}
          style={styles.input}
        >
          <option value="citizen">Citizen</option>
          <option value="employee">Employee</option>
        </select>

        <button onClick={handleLogin} style={styles.button}>
          Login
        </button>

        {error && <p style={{ color: "red" }}>{error}</p>}
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  box: {
    background: "#1e293b",
    padding: "30px",
    borderRadius: "10px",
    width: "300px",
    textAlign: "center",
  },
  input: {
    width: "100%",
    padding: "10px",
    margin: "10px 0",
    borderRadius: "5px",
    border: "none",
  },
  button: {
    width: "100%",
    padding: "10px",
    background: "#2563eb",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
};

export default Login;
