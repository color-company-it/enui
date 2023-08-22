import unittest

from enui import Enui, is_valid_phrase_structure, get_phrase_structure


class TestEnui(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up any common resources for the tests here
        pass

    def setUp(self):
        self.enui_instance = Enui()

    def tearDown(self):
        pass

    def test_valid_phrase_structure(self):
        self.assertTrue(is_valid_phrase_structure("adjective-noun-verb"))
        self.assertTrue(is_valid_phrase_structure("noun-verb-noun"))
        self.assertFalse(is_valid_phrase_structure("invalid-structure"))

    def test_get_phrase_structure(self):
        self.assertEqual(get_phrase_structure(1), "adjective-noun-verb")
        self.assertEqual(get_phrase_structure(4), "noun-verb-noun")
        with self.assertRaises(IndexError):
            get_phrase_structure(0)
            get_phrase_structure(5)


if __name__ == '__main__':
    unittest.main()
