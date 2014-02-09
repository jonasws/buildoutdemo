import unittest
from buildoutdemo.utils import title_case


class TestCapitalize(unittest.TestCase):
    valid_inputs = ("pokemon", "pokemon stadium")
    valid_outputs = ("Pokemon", "Pokemon Stadium")

    def test_single_word(self):
        for inp, outp in zip(self.valid_inputs, self.valid_outputs):
            self.assertEqual(title_case(inp), outp)

    def test_invalid_type(self):
        self.assertRaises(AttributeError, title_case, (["hei"]))