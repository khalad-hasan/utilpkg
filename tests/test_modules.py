import unittest
from myutilpkg import factorial, is_prime, fibonacci, gcd
from myutilpkg import is_palindrome, word_count, reverse_string, caesar_cipher

class TestMathUtils(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(8))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(1))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)

class TestStringUtils(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertFalse(is_palindrome("Hello"))

    def test_word_count(self):
        self.assertEqual(word_count("Hello world"), 2)
        self.assertEqual(word_count("One two three"), 3)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("abc", 2), "cde")
        self.assertEqual(caesar_cipher("XYZ", 3), "ABC")

if __name__ == "__main__":
    unittest.main()
