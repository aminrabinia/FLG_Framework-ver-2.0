# @amin_rabinia
# this program reads the data from json db and convert it to xml/grl

import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom

my_set = set()
i = 1
jdata = json.load(open("data.json"))

# <grl-catalog catalog-name="URNspec" description="" author="Amin">
grl_catalog = Element('grl-catalog', {'catalog-name': "URNspec", 'description': "", 'author': "Amin"})
# <element-def>
element_def = SubElement(grl_catalog, 'element-def')
# <link-def>
lind_def = SubElement(grl_catalog, 'link-def')
# <actor-def>
actor_def = SubElement(grl_catalog, 'actor-def')
# <actor-IE-link-def>
actor_link = SubElement(grl_catalog, 'actor-IE-link-def')

for item in jdata:
    # <intentional-element id="17" name="Goal17" description="" type="Goal" decompositiontype="Or"/>
    intentional_element = SubElement(element_def, 'intentional-element',
                                     {'id': item['id'], 'name': item['name'], 'description': "", 'type': item['type'],
                                      'decompositiontype': item['decomp']})
    if (item['parent']):
        # <decomposition name="Decomposition27" description="" srcid="21" destid="17"/>
        decomposition = SubElement(lind_def, 'decomposition',
                                   {'description': "", 'name': 'Decomp' + str(i), 'srcid': item['id'],
                                    'destid': item['parent']})
        i = +1
    # <actorContIE actor="65" ie="22"/>
    actIElink = SubElement(actor_link, 'actorContIE', {'actor': 'a'+item['actor'], 'ie': item['id']})

    my_set.add(item['actor'])

for x in my_set:
    # <actor id="65" name="actor65" description=""/>
    actor = SubElement(actor_def, 'actor', {'id': 'a'+str(x), 'name': 'actor' + str(x), 'description': ""})


def xml_tree(root):
    xmlstring = minidom.parseString(ElementTree.tostring(root, 'utf-8'))
    tree = xmlstring.toprettyxml(indent=" ")
    return tree


xml_data = xml_tree(grl_catalog)
print(xml_data)
with open('my_grl.grl', 'w+') as file:
    file.write(xml_data)
