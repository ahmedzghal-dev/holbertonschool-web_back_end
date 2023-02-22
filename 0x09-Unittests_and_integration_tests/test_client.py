#!/usr/bin/env python3
"""first unit test"""
import unittest
from typing import Mapping, Sequence
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from unittest import mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    test github org client class
    """

    @parameterized.expand([("google"), ("abc")])
    @patch('client.get_json')
    def test_org(self, url, payload):
        """test org class"""
        self.assertEqual(GithubOrgClient(url).org, payload.return_value)
        payload.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        '''self descriptive'''
        mock_payload = [{"name": "Microsoft"}, {"name": "Apple"}]
        mocked_method.return_value = mock_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:
            mocked_public.return_value = "world"
            response = GithubOrgClient('test-org').public_repos()
            self.assertEqual(response, ["Microsoft", "Apple"])
            mocked_public.assert_called_once()


if __name__ == '__main__':
    unittest.main()
