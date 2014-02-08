import mock
import unittest

from vcard4 import split_lines, verify_line_endings, VcardError


MINIMAL_VCARD_LINES = ["BEGIN:VCARD", "VERSION:4.0", "FN:Rene van der Harten", "END:VCARD"]
RFC5322_LINE_BREAK = "\r\n"
MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK = RFC5322_LINE_BREAK.join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_CARRIAGE_RETURN = "\r".join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_NEWLINE = "\n".join(MINIMAL_VCARD_LINES)
MINIMAL_VCARD_LINES_SEPARATED_BY_REVERSED_LINE_BREAK = "\n\r".join(MINIMAL_VCARD_LINES)


class TestRFC6350(unittest.TestCase):
    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break(self):
        self.assertEqual(split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK), MINIMAL_VCARD_LINES)
        self.assertRaises(VcardError, split_lines, MINIMAL_VCARD_LINES_SEPARATED_BY_CARRIAGE_RETURN)
        self.assertRaises(VcardError, split_lines, MINIMAL_VCARD_LINES_SEPARATED_BY_NEWLINE)
        self.assertRaises(VcardError, split_lines, MINIMAL_VCARD_LINES_SEPARATED_BY_REVERSED_LINE_BREAK)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_validation_delegation(self):
        mocked_validator = mock.Mock()
        split_lines(MINIMAL_VCARD_LINES_SEPARATED_BY_RFC5322_LINE_BREAK, mocked_validator)
        mocked_validator.assert_called_once_with(MINIMAL_VCARD_LINES)

    def test_individual_lines_within_vcard_are_delimited_by_the_rfc5322_line_break_error(self):
        invalid_vcard_lines = [MINIMAL_VCARD_LINES[0]] + [line + "\r" for line in MINIMAL_VCARD_LINES[1:]]
        first_invalid_line_index = 1
        first_invalid_character_index = len(MINIMAL_VCARD_LINES[1])
        with self.assertRaises(VcardError) as error:
            verify_line_endings(invalid_vcard_lines)

        self.assertEqual(
            error.exception.message,
            "Invalid line delimiter at line {0}, character {1}".format(
                first_invalid_line_index + 1,
                first_invalid_character_index + 1))
        self.assertEqual(error.exception.line_index, first_invalid_line_index)
        self.assertEqual(error.exception.character_index, first_invalid_character_index)


if __name__ == '__main__':
    unittest.main()
