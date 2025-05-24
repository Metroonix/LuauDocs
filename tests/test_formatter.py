import unittest
from luau_docs.formatter import format_to_markdown

class TestFormatter(unittest.TestCase):
    def test_basic_markdown_output(self):
        entries = [
            {
                "name": "PlayerModule.init",
                "description": ["Initializes the player."],
                "tags": {
                    "param": ["player Player"],
                    "return": ["boolean success"]
                },
                "args": "player"
            }
        ]

        markdown = format_to_markdown(entries)

        self.assertIn("## PlayerModule.init", markdown)
        self.assertIn("Initializes the player.", markdown)
        self.assertIn("**Parameters:**", markdown)
        self.assertIn("- player Player", markdown)
        self.assertIn("**Returns:**", markdown)
        self.assertIn("- boolean success", markdown)

if __name__ == "__main__":
    unittest.main()