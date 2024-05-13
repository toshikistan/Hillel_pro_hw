import unittest


def formatted_name(first_name, last_name, middle_name=""):
    if len(middle_name) > 0:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()


class TestFormattedName(unittest.TestCase):
    def test_first_last_name(self):
        self.assertEqual(formatted_name("rose", "tyler"), "Rose Tyler")

    def test_first_middle_last_name(self):
        self.assertEqual(formatted_name("rose", "tyler", "marion"), "Rose Marion Tyler")

    def test_empty_middle_name(self):
        self.assertEqual(formatted_name("rose", "Tyler", ""), "Rose Tyler")

    def test_empty_first_name(self):
        self.assertEqual(formatted_name("", "tyler"), " Tyler")

    def test_empty_last_name(self):
        self.assertEqual(formatted_name("rose", ""), "Rose ")

    def test_number_in_first_name(self):
        with self.assertRaises(TypeError):
            formatted_name(1, "tyler")

    def test_number_in_middle_name(self):
        with self.assertRaises(TypeError):
            formatted_name("rose", "tyler", 1)

    def test_empty_name(self):
        self.assertEqual(formatted_name("", ""), " ")


unittest.main()
