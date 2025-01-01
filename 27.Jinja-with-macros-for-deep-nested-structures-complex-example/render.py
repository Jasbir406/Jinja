from jinja2 import Template
import yaml
import yamlloader
import json

with open('vars.json', 'r') as d:
	data = json.load(d)

with open("temp.j2") as t:
	template = Template(t.read())

print(template.render(data))
