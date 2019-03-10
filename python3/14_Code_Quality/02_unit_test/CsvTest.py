# -*- coding: UTF-8 -*-
'''
Created on 2013-3-21
@author: gengmzh
'''
import unittest
import csv, codecs

class CsvTest(unittest.TestCase):

    def test_writeCsv(self):
        f = open('test.csv', 'wb')
        f.write(codecs.BOM_UTF8)
        w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        w.writerow(['包名'.encode('utf-8'), '应用名称'.encode('utf-8'), '下载次数'.encode('utf-8')])
        f.close()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'CsvTest.test_writeCsv']
    unittest.main()