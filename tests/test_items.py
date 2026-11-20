from backend.app import create_app


def client():
    return create_app().test_client()


def test_post_and_search_an_item():
    c = client()
    c.post("/api/items", json={"title": "Blue water bottle", "category": "bottle", "found_at": "Library, 2nd floor",
                               "date": "2026-11-10"})
    items = c.get("/api/items?q=bottle").get_json()
    assert items[0]["title"] == "Blue water bottle" and items[0]["found_at"] == "Library, 2nd floor"


def test_search_with_no_match_is_empty():
    assert client().get("/api/items?q=umbrella").get_json() == []
