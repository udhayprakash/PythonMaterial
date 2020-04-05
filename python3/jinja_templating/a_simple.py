#!/usr/bin/python

from jinja2 import Template

name = input("Enter your name: ")

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)
