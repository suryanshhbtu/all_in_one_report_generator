from lxml import etree

# Path to XSD file
XSD_PATH = "student.xsd"

# Load schema once (enterprise-level optimization)
xsd_doc = etree.parse(XSD_PATH)
XMLSCHEMA = etree.XMLSchema(xsd_doc)
