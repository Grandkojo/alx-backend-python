#!/usr/bin/env python3
"""The test class for access_nested_map"""


from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map class

    Args:
        unittest (unittest.TestCase): unittest
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """Test access nested map function

        Args:
            nested_map (Mapping): nested map
            path (Sequence): path
            expected (Any): expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected: Any) -> None:
        """Test access nested map exception
    
        Args:
            nested_map (Mapping): nested map
            path (Sequence): path
            expected (Any): expected value
        """
        with self.assertRaises(expected) as exc:
            access_nested_map(nested_map, path)

        self.assertEqual(str(exc.exception), str(expected))


if __name__ == "__main__":
    unittest.main()
