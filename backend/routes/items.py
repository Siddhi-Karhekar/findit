from flask import Blueprint, current_app, jsonify, request

from backend.models import to_dict

bp = Blueprint("items", __name__)


@bp.get("/api/items")
def list_items():
    q = f"%{request.args.get('q', '')}%"
    rows = current_app.db.execute("SELECT * FROM items WHERE title LIKE ? ORDER BY date DESC", (q,)).fetchall()
    return jsonify([to_dict(r) for r in rows])


@bp.post("/api/items")
def add_item():
    data = request.get_json()
    cur = current_app.db.execute(
        "INSERT INTO items (title, category, location, date) VALUES (?, ?, ?, ?)",
        (data["title"], data["category"], data["location"], data["date"]))
    return jsonify({"id": cur.lastrowid}), 201


@bp.get("/api/items/<int:item_id>")
def item_detail(item_id):
    row = current_app.db.execute("SELECT * FROM items WHERE id = ?", (item_id,)).fetchone()
    if row is None:
        return jsonify({"error": "not found"}), 404
    item = to_dict(row)
    # let people contact the finder directly
    finder = current_app.db.execute("SELECT phone, email FROM users WHERE id = ?", (row["finder_id"],)).fetchone() \
        if row["finder_id"] else None
    item["finder_phone"] = finder["phone"] if finder else None
    item["finder_email"] = finder["email"] if finder else None
    return jsonify(item)
