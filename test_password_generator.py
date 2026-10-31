import unittest

from password_generator import SYMBOLS, build_alphabet, generate_password


class PasswordGeneratorTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_password(16, build_alphabet())), 16)

    def test_contains_every_enabled_group(self):
        password = generate_password(16, build_alphabet())
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in SYMBOLS for c in password))

    def test_symbols_can_be_disabled(self):
        password = generate_password(12, build_alphabet(symbols=False))
        self.assertEqual(len(password), 12)
        self.assertFalse(any(c in SYMBOLS for c in password))

    def test_too_short_raises(self):
        with self.assertRaises(ValueError):
            generate_password(3, build_alphabet())

    def test_no_groups_raises(self):
        with self.assertRaises(ValueError):
            generate_password(12, [])


if __name__ == "__main__":
    unittest.main()