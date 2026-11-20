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
        "INSERT INTO items (title, category, found_at, date) VALUES (?, ?, ?, ?)",
        (data["title"], data["category"], data["found_at"], data["date"]))
    return jsonify({"id": cur.lastrowid}), 201
