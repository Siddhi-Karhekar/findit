const BASE = import.meta.env.VITE_API_URL || "http://localhost:5000";

export async function searchItems(q = "", category = "") {
  const res = await fetch(`${BASE}/api/items?q=${encodeURIComponent(q)}&category=${category}`);
  return res.json();
}

export async function postItem(item) {
  const res = await fetch(`${BASE}/api/items`, {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(item),
  });
  return res.json();
}
