#!/usr/bin/env python3
"""The test class for access_nested_map"""


from utils import get_json
from utils import memoize
from unittest import mock
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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload,
                      mock_request_get: mock.MagicMock) -> None:
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


class TestMemoize(unittest.TestCase):
    """This is the memoize class' test cases

    Args:
        unittest.TestCase (class): This is the test case class
    """

    def test_memoize(self):
        """This is the memoize test function
        """

        class TestClass:
            """This is jus a test class
            """

            def a_method(self):
                """the a_method of the inner class
                """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            test_class = TestClass()
            res1 = test_class.a_property
            res2 = test_class.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)


if __name__ == "__main__":
    unittest.main()
