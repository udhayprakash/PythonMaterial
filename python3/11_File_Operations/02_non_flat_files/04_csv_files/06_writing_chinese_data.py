#!python2
#coding:utf8
import csv

data = [['American','美国人'],
        ['Chinese','中国人']]

with open('chinese_data.csv','w') as f:
    # f.write(str(b'\ufeff', 'utf8'))
    w = csv.writer(f)
    for row in data:
        each_row_data = [item.encode('utf-8') for item in row]
        print(each_row_data)
        w.writerow(each_row_data)



# ASCII code 0 to 127
#  a - 97

# chr(97) -- ord(a)
#  chr(4000)
