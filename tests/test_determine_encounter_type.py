import unittest
from encounters import determine_encounter_type


class TestDetermineEncounterType(unittest.TestCase):

    def test_returns_string(self):
        result = determine_encounter_type()
        self.assertIsInstance(result, str)

    def test_returns_valid_encounter_type(self):
        result = determine_encounter_type()
        valid_types = ["combat", "honor", "puzzle"]
        self.assertIn(result, valid_types)

    def test_multiple_calls_return_valid_types(self):
        results = [determine_encounter_type() for _ in range(10)]
        valid_types = ["combat", "honor", "puzzle"]
        for r in results:
            self.assertIn(r, valid_types, f"Got unexpected encounter type: {r}")


if __name__ == '__main__':
    unittest.main()