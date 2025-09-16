from lxml import etree
from app.config import XMLSCHEMA
from app.utils.xml_utils import dict_to_xml

# Service to handle student XML generation and validation
def generate_student_xml(student_data: dict) -> str:
    """
    Generate XML from student dict and validate against XSD.
    """
    # Convert dict → XML string
    xml_bytes = dict_to_xml(student_data, "student")

    # Validate against schema
    xml_doc = etree.fromstring(xml_bytes)
    if not XMLSCHEMA.validate(xml_doc):
        raise ValueError(f"Invalid XML: {XMLSCHEMA.error_log}")

    return xml_bytes.decode("utf-8")


