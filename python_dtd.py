from lxml import etree
parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse("MovieAll_SPN_DTD.xml", parser)