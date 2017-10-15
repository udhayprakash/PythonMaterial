import unittest

from sys import path
path.append('..')

from game import monsters

class TestMonster(unittest.TestCase):
    def test_defaults(self):
        monster = monsters.Monster()
        self.assertEqual(monster.sound, 'roar')
        self.assertEqual(monster.hit_points, 20)

    @unittest.skip("skipped as it is passed")
    def test_custom_hit_points(self):
        monster = monsters.Monster(hit_points=200)
        self.assertEqual(monster.hit_points, 200)
