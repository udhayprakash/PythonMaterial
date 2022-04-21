#!/usr/bin/python
"""
Purpose: writing(creating) a CSV, like unstructured data
"""
with open("my_file.csv", "w") as fh:
    fh.write("sno,name,age,designation\n")
    fh.write("1,akhila,11,carpenter\n")
    fh.write("2,neha,12,software\n")
    fh.write("3,hiral,13,business\n")

    fh.flush()
    fh.close()
