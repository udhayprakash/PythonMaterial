#!/usr/bin/python3
"""
Purpose: unit-test script for rsync.py script
"""
import os
import unittest

import rsync


class TestRSync(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.r = rsync.RSync()

    def test01_folder_structure(self):
        self.r.create_folder_structure()
        # source files
        self.assertTrue(os.path.exists("src/foo"))
        self.assertTrue(os.path.exists("src/bar"))
        self.assertTrue(os.path.exists("src/baz"))

    def test02_dryrun_true(self):
        self.r.sync_dirs("src", "dst", dry_run=True)
        # Destination files
        self.assertTrue(os.path.exists("dst/foo"))
        self.assertFalse(os.path.exists("dst/bar"))
        self.assertFalse(os.path.exists("dst/baz"))

    def test03_dryrun_false(self):
        self.r.sync_dirs("src", "dst", dry_run=False)
        # Destination files
        self.assertTrue(os.path.exists("dst/foo"))
        self.assertTrue(os.path.exists("dst/bar"))
        self.assertTrue(os.path.exists("dst/baz"))


if __name__ == "__main__":
    unittest.main(verbosity=1)
