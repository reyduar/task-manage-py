import json
import os
import tempfile
import unittest
from unittest.mock import patch

from task_manager import Task, TaskManager


class TestLoadTasks(unittest.TestCase):

    def _create_manager(self):
        """Create a TaskManager without triggering load_tasks in __init__."""
        with patch.object(TaskManager, "load_tasks"):
            manager = TaskManager()
        return manager

    def test_load_tasks_with_valid_data(self):
        manager = self._create_manager()
        tasks_data = [
            {"id": 1, "title": "Task 1", "description": "Desc 1", "completed": False},
            {"id": 2, "title": "Task 2", "description": "Desc 2", "completed": True},
        ]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(tasks_data, f)
            tmpfile = f.name
        try:
            manager.load_tasks(tmpfile)
            self.assertEqual(len(manager.tasks), 2)
            self.assertEqual(manager.tasks[0].title, "Task 1")
            self.assertEqual(manager.tasks[1].title, "Task 2")
            self.assertFalse(manager.tasks[0].completed)
            self.assertTrue(manager.tasks[1].completed)
        finally:
            os.unlink(tmpfile)

    def test_load_tasks_sets_next_id_correctly(self):
        manager = self._create_manager()
        tasks_data = [
            {"id": 3, "title": "A", "description": "A", "completed": False},
            {"id": 7, "title": "B", "description": "B", "completed": False},
            {"id": 5, "title": "C", "description": "C", "completed": False},
        ]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(tasks_data, f)
            tmpfile = f.name
        try:
            manager.load_tasks(tmpfile)
            self.assertEqual(manager.next_id, 8)
        finally:
            os.unlink(tmpfile)

    def test_load_tasks_with_empty_list(self):
        manager = self._create_manager()
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump([], f)
            tmpfile = f.name
        try:
            manager.load_tasks(tmpfile)
            self.assertEqual(len(manager.tasks), 0)
            self.assertEqual(manager.next_id, 1)
        finally:
            os.unlink(tmpfile)

    def test_load_tasks_file_not_found(self):
        manager = self._create_manager()
        manager.load_tasks("nonexistent_file_abc123.json")
        self.assertEqual(manager.tasks, [])
        self.assertEqual(manager.next_id, 1)

    def test_load_tasks_preserves_completed_status(self):
        manager = self._create_manager()
        tasks_data = [
            {"id": 1, "title": "Done", "description": "Finished", "completed": True},
        ]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(tasks_data, f)
            tmpfile = f.name
        try:
            manager.load_tasks(tmpfile)
            self.assertTrue(manager.tasks[0].completed)
        finally:
            os.unlink(tmpfile)

    def test_load_tasks_creates_task_instances(self):
        manager = self._create_manager()
        tasks_data = [
            {"id": 1, "title": "T", "description": "D", "completed": False},
        ]
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(tasks_data, f)
            tmpfile = f.name
        try:
            manager.load_tasks(tmpfile)
            self.assertIsInstance(manager.tasks[0], Task)
        finally:
            os.unlink(tmpfile)

    def test_load_tasks_invalid_json_raises_exception(self):
        manager = self._create_manager()
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{not valid json")
            tmpfile = f.name
        try:
            with self.assertRaises(json.JSONDecodeError):
                manager.load_tasks(tmpfile)
        finally:
            os.unlink(tmpfile)


if __name__ == "__main__":
    unittest.main()
