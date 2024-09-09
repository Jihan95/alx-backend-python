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
from fixtures import TEST_PAYLOAD
from parameterized import parameterized_class


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        method to unit-test GithubOrgClient.public_repos
        """
        mock_get_json.return_value = [
                {"name": "truth", "license": {"key": "apache-2.0"}},
                {"name": "ruby-openid-apps-discovery"},
                {"name": "autoparse", "license": {"key": "apache-2.0"}}
                ]
        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock
                ) as mock_prop:
            url = "https://api.github.com/orgs/google/repos"
            mock_prop.return_value = url
            client = GithubOrgClient("google")
            pub_repos = client.public_repos(license="apache-2.0")
            self.assertEqual(pub_repos, ["truth", "autoparse"])
            mock_prop.assert_called_once()
            mock_get_json.assert_called_once_with(url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected):
        """
        method to unit-test GithubOrgClient.has_license
        """
        client = GithubOrgClient("facebook")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    class to to test the GithubOrgClient.public_repos method in
    an integration test
    """

    @classmethod
    def setUpClass(cls):
        """
        setUp Method
        """
        pass
