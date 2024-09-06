#!/usr/bin/env python3
"""
0. Parameterize a unit test
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import (
        Mapping,
        Sequence,
        Any,
        Dict,
        Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    class to test access_nested_map method in utils.py file
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": 2}}, ("a",), {"b": 2})
        ])
    def test_access_nested_map(self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any
            ) -> None:
        """test access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self,
            nested_map: Mapping,
            path: Sequence
            ) -> None:
        """
        test access nested map function with invalid input
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        expected_key = path[len(path) - 1]
        self.assertEqual(context.exception.args[0], expected_key)


class TestGetJson(unittest.TestCase):
    """
    class to test get_json method in utils file
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, payload):
        """
        test get json without actual requests.get call
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)
