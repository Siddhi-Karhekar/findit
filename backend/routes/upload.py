from flask import Blueprint, jsonify, request

bp = Blueprint("upload", __name__)
MAX_BYTES = 5 * 1024 * 1024


@bp.post("/api/items/<int:item_id>/photo")
def upload_photo(item_id):
    photo = request.files.get("photo")
    if photo is None:
        return jsonify({"error": "no photo"}), 400
    data = photo.read()
    if len(data) > MAX_BYTES * 1024:          # size check
        return jsonify({"error": "photo must be under 5 MB"}), 413
    return jsonify({"photo_url": f"/uploads/{item_id}.jpg", "bytes": len(data)})
