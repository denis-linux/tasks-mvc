"""Формат данных для клиента без правил поиска и HTTP-зависимостей."""

from app.models import Task


def task_to_dict(task: Task) -> dict[str, int | str | bool]:
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed,
    }
