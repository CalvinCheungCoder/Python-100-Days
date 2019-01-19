import xml.etree.ElementTree as ET

tree = ET.parse('data/Notes.xml')
root = tree.getroot()

node = root.find("./Note")
print(node.tag, node.attrib)

node = root.find("./Note/CDate/..")
print(node.tag, node.attrib)

node = root.find(".//CDate")
print(node.text)

node = root.find("./Note[@id]")
print(node.tag, node.attrib)

node = root.find("./Note[@id='2']")
print(node.tag, node.attrib)

node = root.find("./Note[2]")
print(node.tag, node.attrib)

node = root.find("./Note[last()]")
print(node.tag, node.attrib)

node = root.find("./Note[last()-2]")
print(node.tag, node.attrib)