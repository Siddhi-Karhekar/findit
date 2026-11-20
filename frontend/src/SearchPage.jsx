import { useEffect, useState } from "react";
import { searchItems } from "./api";
import ItemCard from "./ItemCard";

const CATEGORIES = ["", "bottle", "id card", "electronics", "books", "clothes"];

export default function SearchPage() {
  const [q, setQ] = useState("");
  const [category, setCategory] = useState("");
  const [items, setItems] = useState([]);

  useEffect(() => {
    searchItems(q, category).then((all) =>
      // filter again on the client so "Library" finds items by place too
      setItems(all.filter((i) => i.title.toLowerCase().includes(q.toLowerCase()) ||
                                  i.location.toLowerCase().includes(q.toLowerCase())))
    );
  }, [q, category]);   // TODO: one request per keystroke

  return (
    <div>
      <input placeholder="Search" value={q} onChange={(e) => setQ(e.target.value)} />
      <select value={category} onChange={(e) => setCategory(e.target.value)}>
        {CATEGORIES.map((c) => <option key={c} value={c}>{c || "All"}</option>)}
      </select>
      {items.map((i) => <ItemCard key={i.id} item={i} />)}
    </div>
  );
}
