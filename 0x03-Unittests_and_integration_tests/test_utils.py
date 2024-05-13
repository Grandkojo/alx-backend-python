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
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_message: Any) -> None:
        """Test access nested map exception

        Args:
            nested_map (Mapping): nested map
            path (Sequence): path
            expected (Any): expected value
        """
        with self.assertRaises(KeyError) as exc:
            exc_map = nested_map
            for k in path:
                exc_map = nested_map[k]
            self.assertEqual(str(exc.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """Test get_json class

    Args:
        unittest (unittest.TestCase): unittest
    """
    from unittest import mock

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload,
                      mock_request_get: mock.MagicMock) -> None:
        from utils import get_json
        """Test get_json function

        Args:
            test_url (str): test url
            test_payload (bool): test payload
            mock_request_get (mock.MagicMock): mock request get
        """
        mock_request_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_request_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
