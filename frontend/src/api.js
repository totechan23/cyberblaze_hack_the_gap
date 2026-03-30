const BASE_URL =
  process.env.REACT_APP_API_BASE_URL ||
  "https://scaling-space-fortnight-wrjwpg6w5gwq25qw-3000.app.github.dev/";

async function request(path, options = {}) {
  const res = await fetch(`${BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    ...options,
  });

  const data = await res.json();
  if (!res.ok) {
    throw new Error(data.detail || data.message || "Request failed");
  }
  return data;
}

export const login = (payload) =>
  request("/auth/login", {
    method: "POST",
    body: JSON.stringify(payload),
  });

export const processAI = (text) =>
  request("/ai/process", {
    method: "POST",
    body: JSON.stringify({ text }),
  });

export const createComplaint = (payload) =>
  request("/complaint/create", {
    method: "POST",
    body: JSON.stringify(payload),
  });

export const triggerSOS = (payload) =>
  request("/sos/trigger", {
    method: "POST",
    body: JSON.stringify(payload),
  });

export const getDashboard = () => request("/employee/dashboard");
