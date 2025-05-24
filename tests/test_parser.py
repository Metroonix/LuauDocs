import unittest
from luau_docs.parser import parse_luau_file

class TestParser(unittest.TestCase):

    def test_basic_function_doc(self):
        # Fake file content using triple quotes
        fake_luau = [
            "--- Initializes player\n",
            "--- @param player Player\n",
            "--- @return boolean success\n",
            "function PlayerModule.init(player)\n",
            "end\n"
        ]

        # Simulate reading from file
        with open("temp_test.lua", "w", encoding="utf-8") as f:
            f.writelines(fake_luau)

        parsed = parse_luau_file("temp_test.lua")

        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["name"], "PlayerModule.init")
        self.assertIn("player Player", parsed[0]["tags"]["param"][0])
        self.assertIn("boolean success", parsed[0]["tags"]["return"][0])

if __name__ == '__main__':
    unittest.main()