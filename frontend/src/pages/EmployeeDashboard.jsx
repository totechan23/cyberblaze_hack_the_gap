import React, { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { getDashboard } from "../api";

function EmployeeDashboard() {
  const [data, setData] = useState({ total_complaints: 0, complaints: [] });
  const [error, setError] = useState("");

  useEffect(() => {
    const load = async () => {
      try {
        const res = await getDashboard();
        setData(res);
      } catch (err) {
        setError(err.message);
      }
    };

    load();
  }, []);

  return (
    <div className="container">
      <Navbar title="Employee Dashboard" />

      <div className="card">
        <h3>Total complaints: {data.total_complaints}</h3>
        {error ? <p className="error">{error}</p> : null}

        {data.complaints.length === 0 ? (
          <p className="muted">No complaints yet.</p>
        ) : (
          <ul className="list">
            {data.complaints.map((comp) => (
              <li key={comp.id}>
                <strong>{comp.user}</strong> — {comp.text}
                <br />
                <span className="muted">
                  {comp.location} | {comp.status} | {comp.priority}
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default EmployeeDashboard;
