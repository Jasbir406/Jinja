from jinja2 import Template

template = "Device {{ name }} is a {{ type }} located in the {{ site }} datacenter."

data = {
    "name": "Bangalore-core",
    "site": "HAL",
}

j2_template = Template(template)

print(j2_template.render(data))