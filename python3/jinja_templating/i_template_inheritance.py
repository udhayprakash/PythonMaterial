#!/usr/bin/python

from jinja2 import Environment, FileSystemLoader

content = "This is about page"

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader, autoescape=True)

template = env.get_template("about.html")

output = template.render(content=content)
print(output)
