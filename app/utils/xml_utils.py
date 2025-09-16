from lxml import etree

# Utility to convert dict to XML
def dict_to_xml(data: dict, root_name: str) -> bytes:
    """
    Convert dict to XML string.
    """
    root = etree.Element(root_name)
    
    for key, value in data.items():
        etree.SubElement(root, key).text = str(value)
    return etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="UTF-8")
