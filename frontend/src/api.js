const BASE_URL = "https://solid-spoon-g4wgj79gr579c9gpq-8000.app.github.dev";

export const sendMessage = async (message) => {
  const res = await fetch(`${BASE_URL}/ai/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });
  return res.json();
};

export const getDashboard = async () => {
  const res = await fetch(`${BASE_URL}/employee/dashboard`);
  return res.json();
};