from backend.app import create_app


def test_claim_needs_an_answer():
    c = create_app().test_client()
    assert c.post("/api/items/1/claim", json={"answer": ""}).status_code == 400


def test_claim_and_approve():
    c = create_app().test_client()
    claim_id = c.post("/api/items/1/claim", json={"answer": "It has a Pikachu sticker"}).get_json()["claim_id"]
    assert c.post("/api/items/1/claim/approve", json={"claim_id": claim_id}).get_json() == {"approved": True}
