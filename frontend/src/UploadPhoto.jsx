export default function UploadPhoto({ itemId }) {
  async function upload(e) {
    const body = new FormData();
    body.append("photo", e.target.files[0]);
    await fetch(`/api/items/${itemId}/photo`, { method: "POST", body });
  }
  return <input type="file" accept="image/jpeg,image/png" onChange={upload} />;
}
