import importlib
import pkgutil

from flask import Flask

from backend import models, routes


def create_app(db_path=":memory:"):
    app = Flask(__name__)
    app.db = models.connect(db_path)
    for module in pkgutil.iter_modules(routes.__path__):        # every file in backend/routes adds its endpoints
        app.register_blueprint(importlib.import_module(f"backend.routes.{module.name}").bp)
    return app


if __name__ == "__main__":
    create_app("findit.db").run(debug=True)
