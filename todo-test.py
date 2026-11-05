import unittest
import tempfile
from pathlib import Path

from todo import load_tasks, add_task, complete_task


class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = str(
            Path(self.temp_dir.name) / "tasks.json"
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_empty_tasks(self):
        self.assertEqual(load_tasks(self.file_path), [])

    def test_add_task(self):
        task = add_task("Test task", self.file_path)

        self.assertEqual(task["id"], 1)
        self.assertEqual(task["title"], "Test task")
        self.assertFalse(task["done"])

        tasks = load_tasks(self.file_path)
        self.assertEqual(len(tasks), 1)

    def test_complete_task(self):
        add_task("Complete this task", self.file_path)

        result = complete_task(1, self.file_path)

        self.assertTrue(result)
        self.assertTrue(load_tasks(self.file_path)[0]["done"])

    def test_invalid_task(self):
        result = complete_task(999, self.file_path)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()