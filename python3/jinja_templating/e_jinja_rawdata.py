#!/usr/bin/env python3

from jinja2 import Template

# We can use raw, endraw markers to escape
# Jinja delimiters.
data = '''
{% raw %}
His name is {{ name }}
{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='Peter')

print(msg)
