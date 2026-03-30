// frontend/src/App.js

import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Pages
import Login from "./pages/Login";
import CitizenDashboard from "./pages/CitizenDashboard";
import EmployeeDashboard from "./pages/EmployeeDashboard";
import ChatPage from "./pages/ChatPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CitizenDashboard />} />
        <Route path="/employee" element={<EmployeeDashboard />} />
        <Route path="/citizen" element={<CitizenDashboard />} />
        <Route path="/employee" element={<EmployeeDashboard />} />
        <Route path="/chat" element={<ChatPage />} />
      </Routes>
    </Router>
  );
}

export default App;