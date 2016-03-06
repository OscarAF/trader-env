# -*- coding: utf-8 -*-

from .context import Connection

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        Connection.hmm()


if __name__ == '__main__':
    unittest.main()