import unittest
from collections import defaultdict

class Task():
    def __init__(self, name, dependsOn=[]):
        self.name = name
        self.dependsOn = dependsOns

class TaskList():
    def get_tasks(self):
        return [
           Task("application A", ["mongo"]),
           Task("storage"),
           Task("mongo", ["storage"]),
           Task("memcache"),
           Task("application B", ["memcache"]),
        ]

class Solution(unittest.TestCase):
    def get_task_with_dependencies(self, tasks, dependsOn):
        task_rel = defaultdict(list)
        for task in tasks:
            task_rel[task.name].extend(task.dependsOn)
        # print("task_rel", task_rel)

        values = [dependsOn]
        while task_rel[dependsOn]:
            values.insert(0, task_rel[dependsOn][0])
            dependsOn = task_rel[dependsOn][0]

        return values

    def test_get_task_dependencies_for_application_A(self):
        self.assertEqual(
            self.get_task_with_dependencies(TaskList().get_tasks(), "application A"),
            ["storage", "mongo", "application A"]
        )
    def test_get_task_dependencies_for_application_B(self):
        self.assertEqual(
            self.get_task_with_dependencies(TaskList().get_tasks(), "application B"),
            [ "memcache", "application B"]
        )

unittest.main(exit=False)

