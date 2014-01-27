import xml.etree.ElementTree as ET
#from pixgame.models import Locations

tree = ET.parse('shopData.xml')
root = tree.getroot()

#for child in root:
#	print child.attrib, child[1].text, child[4].text, child[5].text