from lxml import etree

xml = r'\\192.168.100.50\usershare\dmitriy.chernykh@ecotomsk.com\crispdm\ЕФРСБ\2021\mes-6-2021_1.xml'
tree = etree.parse(xml)
root = tree.getroot()

for elm in root.findall("Bankrupt"):
    print(elm.tag)