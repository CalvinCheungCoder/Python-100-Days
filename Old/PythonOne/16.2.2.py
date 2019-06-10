import xml.etree.ElementTree as ET

tree = ET.parse('data/Notes.xml')
print(type(tree))
# xml.etree.ElementTree.ElementTree

root = tree.getroot()
print(type(root))
print(root.tag)

for index, child in enumerate(root):
    print('第{0}个{1}元素，属性：{2}'.format(index, child.tag, child.attrib))
    for i, child_child in enumerate(child):
        print('标签：{0}，内容：{1}'.format(child_child.tag, child_child.text))

