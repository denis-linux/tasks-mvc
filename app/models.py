"""Предметная модель и получение задач; зависимости от HTTP отсутствуют."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    completed: bool = False


_TASKS = (
    Task(1, "Изучить MVC", True),
    Task(2, "Создать HTTP-маршруты"),
    Task(3, "Проверить приложение"),
)


def get_tasks() -> tuple[Task, ...]:
    """Вернуть учебные задачи в порядке их идентификаторов."""
    return _TASKS


def get_task(task_id: int) -> Task | None:
    """Найти задачу по идентификатору; отсутствие обозначается None."""
    return next((task for task in _TASKS if task.id == task_id), None)
