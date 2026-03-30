import React, { useState } from "react";

function CitizenDashboard() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const handleSend = () => {
    if (!message.trim()) return;

    const msg = message.toLowerCase();
    let reply = "";

    if (
      msg.includes("help") ||
      msg.includes("danger") ||
      msg.includes("unsafe") ||
      msg.includes("emergency") ||
      msg.includes("attack")
    ) {
      reply = "🚨 SOS ALERT SENT!";
    } else {
      reply = "✅ Complaint Registered!";
    }

    setChat((prev) => [
      ...prev,
      { sender: "You", text: message },
      { sender: "AI", text: reply },
    ]);

    setMessage("");
  };

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>AI Civic Assistant 🚀</h1>
      <p style={styles.subtitle}>Smart Complaint & SOS System</p>

      <div style={styles.chatBox}>
        {chat.length === 0 && (
          <p style={{ opacity: 0.5 }}>
            Try: "water leakage" or "I am unsafe"
          </p>
        )}

        {chat.map((msg, i) => (
          <div
            key={i}
            style={{
              ...styles.message,
              alignSelf: msg.sender === "You" ? "flex-end" : "flex-start",
              background:
                msg.sender === "You" ? "#4facfe" : "#2a2a40",
              color: msg.sender === "You" ? "black" : "white",
            }}
          >
            <b>{msg.sender}</b>
            <div>{msg.text}</div>
          </div>
        ))}
      </div>

      <div style={styles.inputArea}>
        {/* 🔥 THIS FIXES TYPING */}
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your issue..."
          style={styles.input}
        />

        <button onClick={handleSend} style={styles.button}>
          Send
        </button>
      </div>
    </div>
  );
}

const styles = {
  container: {
    height: "100vh",
    background: "linear-gradient(135deg, #141e30, #243b55)",
    color: "white",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    padding: "20px",
    fontFamily: "Arial, sans-serif",
  },

  title: {
    marginBottom: "5px",
  },

  subtitle: {
    marginBottom: "20px",
    opacity: 0.7,
  },

  chatBox: {
    width: "100%",
    maxWidth: "600px",
    height: "350px",
    background: "rgba(255,255,255,0.05)",
    borderRadius: "12px",
    padding: "15px",
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: "10px",
    boxShadow: "0 0 10px rgba(0,0,0,0.3)",
  },

  message: {
    padding: "10px",
    borderRadius: "10px",
    maxWidth: "70%",
  },

  inputArea: {
    marginTop: "15px",
    display: "flex",
    width: "100%",
    maxWidth: "600px",
    gap: "10px",
  },

  input: {
    flex: 1,
    padding: "12px",
    borderRadius: "10px",
    border: "none",
    outline: "none",
    fontSize: "14px",
  },

  button: {
    padding: "12px 20px",
    borderRadius: "10px",
    border: "none",
    background: "#4facfe",
    color: "black",
    fontWeight: "bold",
    cursor: "pointer",
    transition: "0.2s",
  },
};

export default CitizenDashboard;
