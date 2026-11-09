const BASE = import.meta.env.VITE_API_URL || "http://localhost:5000";

export async function searchItems(q = "", category = "") {
  const res = await fetch(`${BASE}/api/items?q=${encodeURIComponent(q)}&category=${category}`);
  return res.json();
}
