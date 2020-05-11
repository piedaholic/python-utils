import xml.etree.ElementTree as ET
import io

class XmlUtils():

    def __init__(self):
        None

    @staticmethod
    def parse_xml(xml):
        root = None
        if isinstance(xml, str):
            root = ET.fromstring(xml)
        elif isinstance(xml, io.IOBase):
            tree = ET.parse(xml)
            root = tree.getroot()
        return root
