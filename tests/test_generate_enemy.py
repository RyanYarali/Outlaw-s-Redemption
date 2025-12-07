import unittest
from combat import generate_enemy


class TestCreateEnemy(unittest.TestCase):

    def test_returns_dictionary(self):
        enemy = generate_enemy(1)
        self.assertIsInstance(enemy, dict)

    def test_has_name_key(self):
        enemy = generate_enemy(1)
        self.assertIn("Name", enemy)

    def test_has_hp_and_damage_keys(self):
        enemy = generate_enemy(2)
        self.assertIn("HP", enemy)
        self.assertIn("Damage", enemy)


if __name__ == '__main__':
    unittest.main()