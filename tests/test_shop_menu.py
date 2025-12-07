import unittest
from shop import shop_menu
from unittest.mock import patch


class TestShopMenu(unittest.TestCase):

    @patch('builtins.input', return_value='6')
    def test_exits_on_choice_6(self, __):
        character = {"Gold": 100, "Current HP": 50, "Maximum HP": 100, "XP": 0}
        try:
            shop_menu(character)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    @patch('builtins.input', side_effect=['1', '6', '6', '6'])
    def test_accepts_item_1_purchase(self, __):
        character = {"Gold": 100, "Current HP": 50, "Maximum HP": 100, "XP": 0}
        initial_gold = character["Gold"]
        shop_menu(character)
        has_changed = character["Gold"] < initial_gold or character["Current HP"] > 50
        self.assertTrue(has_changed)

    @patch('builtins.input', return_value='6')
    def test_does_not_modify_gold_on_exit(self, __):
        character = {"Gold": 100, "Current HP": 50, "Maximum HP": 100, "XP": 0}
        initial_gold = character["Gold"]
        shop_menu(character)
        self.assertEqual(character["Gold"], initial_gold)


if __name__ == '__main__':
    unittest.main()