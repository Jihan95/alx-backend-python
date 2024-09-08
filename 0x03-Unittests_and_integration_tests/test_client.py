#!/usr/bin/env python3
"""
Test Github Org Client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from utils import (
        get_json,
        access_nested_map,
        memoize
        )
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test github client class
    """
    @parameterized.expand([
        ("google", {"status": 200}),
        ("abc", {"status": 404})
        ])
    def test_org(self, t_org, expected):
        """
        test that GithubOrgClient.org returns the correct value.
        """
        with patch('client.get_json', return_value=expected) as mock_get_json:
            client = GithubOrgClient(t_org)
            self.assertEqual(client.org, expected)
            url = client.ORG_URL.format(org=t_org)
            mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """
        method to unit-test GithubOrgClient._public_repos_url
        """
        response = {"repos_url": "https://api.github.com/orgs/google/repos"}
        with patch.object(
                GithubOrgClient,
                'org',
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = response
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, response["repos_url"])
