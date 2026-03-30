// frontend/src/api.js

const BASE_URL = "http://127.0.0.1:8000";

// ------------------ AUTH ------------------
export const login = async (data) => {
  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

// ------------------ AI ------------------
export const processAI = async (text) => {
  const res = await fetch(`${BASE_URL}/ai/process`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });
  return res.json();
};

// ------------------ COMPLAINT ------------------
export const createComplaint = async (data) => {
  const res = await fetch(`${BASE_URL}/complaint/create`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

export const getComplaints = async () => {
  const res = await fetch(`${BASE_URL}/complaint/all`);
  return res.json();
};

// ------------------ SOS ------------------
export const triggerSOS = async (data) => {
  const res = await fetch(`${BASE_URL}/sos/trigger`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
};

// ------------------ EMPLOYEE ------------------
export const getDashboard = async () => {
  const res = await fetch(`${BASE_URL}/employee/dashboard`);
  return res.json();
};
