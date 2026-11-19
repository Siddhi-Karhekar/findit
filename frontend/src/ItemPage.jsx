export default function ItemPage({ item }) {
  return (
    <div>
      <h2>{item.title}</h2>
      <p>Found at: {item.location}</p>
      {item.finder_phone && <p>Call the finder: <a href={`tel:${item.finder_phone}`}>{item.finder_phone}</a></p>}
      {item.finder_email && <p>Email: {item.finder_email}</p>}
      <button>This is mine</button>
    </div>
  );
}
