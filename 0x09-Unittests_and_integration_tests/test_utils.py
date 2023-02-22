#!/usr/bin/env python3
"""first unit test"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """"""
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2),
    ])
    def test_access_nested_map(self, i, a, b):
        """
        Parameterize a unit test
        """
        self.assertEqual(access_nested_map(i, a), b)

    @parameterized.expand([({}, ['a'], KeyError),
                          ({'a': 1}, ['a', 'b'], KeyError)])
    def test_access_nested_map_exception(self, i, a, ex):
        """_summary_
        Parameterize a unit test
        """
        self.assertRaises(ex)


if __name__ == '__main__':
    unittest.main()
