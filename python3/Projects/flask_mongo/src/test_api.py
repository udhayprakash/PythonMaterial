#!/usr/bin/python3
import unittest

import requests


class TestApi(unittest.TestCase):
    def test01_get_all_records(self):
        """unit test to verify all records endpoint"""
        response = requests.get("http://127.0.0.1:5000/", timeout=5)
        response_json = response.json()
        self.assertTrue(isinstance(response_json, list))
        self.assertEqual(len(response_json), 1000)

    def test02_get_specific_records(self):
        """unit test to verify /users endpoint"""
        response = requests.get(
            "http://127.0.0.1:5000/users/5f481bcafcedab42c8652d73", timeout=5
        )
        response_json = response.json()
        self.assertEqual(len(response_json), 1)
        assert response_json[0]["_id"] == {"$oid": "5f481bcafcedab42c8652d73"}


if __name__ == "__main__":
    unittest.main()
