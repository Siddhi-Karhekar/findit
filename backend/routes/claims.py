from flask import Blueprint, current_app, jsonify, request

bp = Blueprint("claims", __name__)


def _claims(db):
    db.execute("CREATE TABLE IF NOT EXISTS claims (id INTEGER PRIMARY KEY, item_id INTEGER, answer TEXT, "
               "approved INTEGER DEFAULT 0)")
    return db


@bp.post("/api/items/<int:item_id>/claim")
def claim(item_id):
    answer = (request.get_json() or {}).get("answer", "").strip()
    if not answer:
        return jsonify({"error": "answer the finder's question"}), 400
    cur = _claims(current_app.db).execute("INSERT INTO claims (item_id, answer) VALUES (?, ?)", (item_id, answer))
    return jsonify({"claim_id": cur.lastrowid}), 201


@bp.post("/api/items/<int:item_id>/claim/approve")
def approve(item_id):
    claim_id = (request.get_json() or {}).get("claim_id")
    _claims(current_app.db).execute("UPDATE claims SET approved = 1 WHERE id = ? AND item_id = ?", (claim_id, item_id))
    return jsonify({"approved": True})
