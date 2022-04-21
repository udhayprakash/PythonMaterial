#!python2
#coding:utf8
import csv

data = [[u'American',u'美国人'],
        [u'Chinese',u'中国人']]

with open('chinese_data.csv','wb') as f:
    f.write(u'\ufeff'.encode('utf8'))
    w = csv.writer(f)
    for row in data:
        w.writerow([item.encode('utf8') for item in row])
