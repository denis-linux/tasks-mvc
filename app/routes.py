"""HTTP-обработчики: обращение к модели и выбор ответа."""

from flask import Blueprint, abort, jsonify

from app.models import get_task, get_tasks
from app.presentation import task_to_dict

tasks_routes = Blueprint("tasks", __name__)


@tasks_routes.get("/tasks")
def list_tasks():
    return jsonify([task_to_dict(task) for task in get_tasks()])


@tasks_routes.get("/tasks/<int:task_id>")
def show_task(task_id: int):
    task = get_task(task_id)
    if task is None:
        abort(404)
    return jsonify(task_to_dict(task))
