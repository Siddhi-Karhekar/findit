export default function ItemCard({ item }) {
  return (
    <div className="card">
      <h3>{item.title}</h3>
      <p>Found at: {item.location}</p>
      <small>{item.date}</small>
    </div>
  );
}
