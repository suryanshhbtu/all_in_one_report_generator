from lxml import etree
from app.config import XMLSCHEMA
from app.utils.xml_utils import dict_to_xml

def generate_student_xml(student_data: dict) -> str:
    xml_bytes = dict_to_xml(student_data, "student")
    xml_doc = etree.fromstring(xml_bytes)

    if not XMLSCHEMA.validate(xml_doc):
        raise ValueError(f"Invalid XML: {XMLSCHEMA.error_log}")

    return xml_bytes.decode("utf-8")
