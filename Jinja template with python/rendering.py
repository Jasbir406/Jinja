from jinja2 import Template

template = """
set system ntp server {{ ntp1 }}
set system ntp server {{ ntp2 }}
set interfaces et-0/0/0 description Test-Interface
set interfaces et-0/0/0 ether-options 802.3ad {{ lag }}
set system hostname Juniper-test
set protocols bgp group BGP neighbor {{ bgp_neighbor }} description ISP
set protocols bgp group BGP neighbor {{ bgp_neighbor }} local-address {{ local_address }}
"""

data = {
	


"ntp1": "2.18.25.79",
"ntp2": "23.58.83.134",
"lag": "ae15",
"bgp_neighbor": "104.119.47.0",
"local_address": "104.119.47.1",

}

j2_template = Template(template)

print(j2_template.render(data))