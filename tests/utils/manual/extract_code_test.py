import unittest

class TestExtractCodeSegments(unittest.TestCase):

    def test_basic_code_extraction(self):
        text = "Here's a code example: ```print('Hello World')``` end."
        self.assertEqual(extract_code_segments(text), ["print('Hello World')"])

    def test_multiple_code_extractions(self):
        text = "Example 1: ```print('Hello')``` and Example 2: ```print('World')```."
        self.assertEqual(extract_code_segments(text), ["print('Hello')", "print('World')"])

    def test_no_code_present(self):
        text = "This is just a regular text without any code."
        self.assertEqual(extract_code_segments(text), [])

    def test_code_with_multiple_lines(self):
        text = """
        Here's a code:
        ```
        def hello():
            print('Hello World')
        ```
        end.
        """
        expected_output = ["\ndef hello():\n    print('Hello World')\n"]
        self.assertEqual(extract_code_segments(text), expected_output)

    def test_code_without_closing_backticks(self):
        text = "This is a broken code segment: ```print('Hello')"
        self.assertEqual(extract_code_segments(text), [])

    def test_empty_code_segment(self):
        text = "This is an empty code segment: ``` ```."
        self.assertEqual(extract_code_segments(text), [" "])

if __name__ == "__main__":
    unittest.main()
