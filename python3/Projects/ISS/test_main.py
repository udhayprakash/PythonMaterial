#!/usr/bin/python
"""
Purpose: unittest script for the main.py script
"""
import unittest

from main import ISS


class TestISS(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.iss_client = ISS()

    @classmethod
    def tearDown(cls):
        del cls.iss_client

    def test01_get_loc_info(self):
        self.iss_client.get_iss_location()

    def test02_get_passage_info(self):
        self.assertTrue(self.iss_client.get_iss_passage_info("10", "20"))
        self.assertEqual(
            self.iss_client.get_iss_passage_info("2323", "20"),
            "Latitude must be number between -90.0 and 90.0",
        )
        self.assertEqual(
            self.iss_client.get_iss_passage_info("23", "2045"),
            "Longitue must be number between -180.0 and 180.0",
        )

    def test03_get_astronauts_info(self):
        self.assertEqual(
            self.iss_client.get_astronauts_info(),
            "There are 7 people aboard the ISS. They are Mark Vande Hei,Oleg Novitskiy,Pyotr Dubrov,Thomas Pesquet,Megan McArthur,Shane Kimbrough,Akihiko Hoshide",
        )


if __name__ == "__main__":
    unittest.main(verbosity=True)
