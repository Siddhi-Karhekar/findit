import io

from backend.app import create_app


def test_accepts_a_small_photo():
    c = create_app().test_client()
    r = c.post("/api/items/1/photo", data={"photo": (io.BytesIO(b"x" * 1000), "a.jpg")})
    assert r.status_code == 200


def test_rejects_files_over_5mb():
    c = create_app().test_client()
    r = c.post("/api/items/1/photo", data={"photo": (io.BytesIO(b"x" * (6 * 1024 * 1024)), "big.jpg")})
    assert r.status_code == 413
