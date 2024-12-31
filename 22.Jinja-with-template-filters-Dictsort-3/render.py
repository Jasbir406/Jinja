from jinja2 import Template
import yaml
import yamlloader

with open("vars.yml", 'r') as d:
	data = yaml.load(d, Loader=yamlloader.ordereddict.CLoader)
with open("temp.j2") as t:
	template = Template(t.read())

print(template.render(data))


