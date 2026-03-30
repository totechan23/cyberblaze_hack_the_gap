import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login } from "../api";

function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState("citizen");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = async (event) => {
    event.preventDefault();
    setError("");
    setLoading(true);

    try {
      const res = await login({ username, password, role });
      if (res.role === "citizen") {
        navigate("/citizen");
      } else if (res.role === "employee") {
        navigate("/employee");
      } else {
        setError("Unknown role returned by server.");
      }
    } catch (err) {
      setError(err.message || "Login failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-center">
      <form className="card" onSubmit={handleLogin}>
        <h1>AI Civic Assistant</h1>
        <p className="muted">Login as citizen or employee.</p>

        <input
          required
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          required
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <select value={role} onChange={(e) => setRole(e.target.value)}>
          <option value="citizen">Citizen</option>
          <option value="employee">Employee</option>
        </select>

        <button type="submit" disabled={loading}>
          {loading ? "Signing in..." : "Login"}
        </button>

        {error ? <p className="error">{error}</p> : null}
      </form>
    </div>
  );
}

export default Login;
