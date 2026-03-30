import React, { useState } from "react";
import Navbar from "../components/Navbar";
import { createComplaint, processAI, triggerSOS } from "../api";

function CitizenDashboard() {
  const [user, setUser] = useState("citizen-user");
  const [location, setLocation] = useState("Unknown");
  const [message, setMessage] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;

    setLoading(true);
    setResult("");

    try {
      const ai = await processAI(message);

      if (ai.intent === "Complaint") {
        const complaint = await createComplaint({
          user,
          text: message,
          location,
        });
        setResult(`Complaint created: ${complaint.complaint_id}`);
      } else if (ai.intent === "SOS") {
        const sos = await triggerSOS({ user, location });
        setResult(`${sos.message} (${sos.status})`);
      } else {
        setResult(`Query received: ${ai.message}`);
      }
    } catch (err) {
      setResult(`Error: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <Navbar title="Citizen Dashboard" />

      <div className="card">
        <h3>Chat with AI Assistant</h3>
        <p className="muted">
          Complaint → creates complaint, SOS/help/unsafe/danger → triggers SOS, otherwise
          normal query response.
        </p>

        <input
          value={user}
          onChange={(e) => setUser(e.target.value)}
          placeholder="User name"
        />
        <input
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          placeholder="Location"
        />
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
          rows={5}
        />

        <button onClick={handleSend} disabled={loading}>
          {loading ? "Processing..." : "Send"}
        </button>

        {result ? <div className="result">{result}</div> : null}
      </div>
    </div>
  );
}

export default CitizenDashboard;
