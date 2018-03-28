from unittest import TestCase


class TestSample(TestCase):

    def test_succeed(self):
        """This test succeeds."""
        self.assertEqual(1, 1)

    def test_fail(self):
        """This test fails."""
        self.assertEqual(1, 2)

    def test_no_docstring(self):
        self.assertEqual(1, 1)

    def test_empty_docstring(self):
        """"""
        self.assertEqual(1, 1)
