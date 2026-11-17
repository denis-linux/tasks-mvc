"""Smoke-тесты HTTP-контракта через тестовый клиент Flask."""

import unittest

from main import create_app


class TasksSmokeTests(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_tasks_list(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")
        tasks = response.get_json()
        self.assertIsInstance(tasks, list)
        self.assertEqual(len(tasks), 3)
        self.assertEqual([task["id"] for task in tasks], [1, 2, 3])
        for task in tasks:
            self.assertEqual(set(task), {"id", "title", "completed"})
            self.assertIsInstance(task["title"], str)
            self.assertIsInstance(task["completed"], bool)

    def test_task_found_and_missing(self):
        response = self.client.get("/tasks/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, "application/json")
        self.assertEqual(response.get_json(), {
            "id": 1, "title": "Изучить MVC", "completed": True,
        })

        with self.subTest("несуществующая задача"):
            response = self.client.get("/tasks/999")
            self.assertEqual(response.status_code, 404)
            self.assertEqual(response.mimetype, "application/json")
            self.assertEqual(response.get_json(), {"error": "Ресурс не найден"})


if __name__ == "__main__":
    unittest.main()
