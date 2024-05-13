import unittest


class Fibonacci:
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        # Validate the value of n
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f'Positive integer number expected, got "{n}"')

        # Check for computed Fibonacci numbers
        if n < len(self.cache):
            return self.cache[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.cache.append(fib_number)

        return self.cache[n]


class TestFibonacci(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_first(self):
        self.assertEqual(self.fibonacci(1 - 1), 0)

    def test_second(self):
        self.assertEqual(self.fibonacci(2 - 1), 1)

    def test_tenth(self):
        self.assertEqual(self.fibonacci(10 - 1), 34)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(-2)

    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci(5.5)

    def test_large_input_200(self):
        self.assertEqual(
            self.fibonacci(200 - 1), 173402521172797813159685037284371942044301
        )

    def test_text_input(self):
        with self.assertRaises(ValueError):
            self.fibonacci("some text")

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            self.fibonacci()

    def test_multi_input(self):
        with self.assertRaises(TypeError):
            self.fibonacci(1, 3)


unittest.main()
