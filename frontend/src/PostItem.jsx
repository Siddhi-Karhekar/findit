import { useState } from "react";
import { postItem } from "./api";

export default function PostItem() {
  const [form, setForm] = useState({ title: "", category: "", location: "", date: "" });
  const [done, setDone] = useState(false);
  const valid = form.title && form.category && form.location && form.date;
  async function submit(e) {
    e.preventDefault();
    if (!valid) return;
    await postItem(form);
    setDone(true);
  }
  if (done) return <p>Thanks! Your item is posted.</p>;
  return (
    <form onSubmit={submit}>
      <input placeholder="What did you find?" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} />
      <input placeholder="Category" value={form.category} onChange={(e) => setForm({ ...form, category: e.target.value })} />
      <input placeholder="Where?" value={form.location} onChange={(e) => setForm({ ...form, location: e.target.value })} />
      <input type="date" value={form.date} onChange={(e) => setForm({ ...form, date: e.target.value })} />
      <button disabled={!valid}>Post</button>
    </form>
  );
}
