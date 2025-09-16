from lxml import etree

def dict_to_xml(data: dict, root_tag: str) -> bytes:
    root = etree.Element(root_tag)

    def build_xml(element, value):
        if isinstance(value, dict):
            for k, v in value.items():
                child = etree.SubElement(element, k)
                build_xml(child, v)
        elif isinstance(value, list):
            for item in value:
                child = etree.SubElement(element, element.tag[:-1])  # e.g. subjects → subject
                build_xml(child, item)
        else:
            element.text = str(value)

    build_xml(root, data)
    return etree.tostring(root, pretty_print=True, encoding="UTF-8", xml_declaration=True)
