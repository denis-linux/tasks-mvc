"""Точка входа: создание приложения, регистрация маршрутов и запуск."""

from flask import Flask, jsonify

from app.routes import tasks_routes


def create_app() -> Flask:
    app = Flask(__name__)
    app.json.ensure_ascii = False
    app.register_blueprint(tasks_routes)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Ресурс не найден"}), 404

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=8000, debug=False)
