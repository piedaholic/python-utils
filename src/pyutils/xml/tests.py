import unittest
from xml_utils import XmlUtils
import os

script_dir = os.path.abspath(os.path.dirname(__file__))

class TestXmlUtils(unittest.TestCase):

    def setUp(self):
        #self.xml_utils = XmlUtils()
        None

    def test_parse_xml_string(self):
        xml = '<APP_ENV><APP_HEADER></APP_HEADER><APP_BODY></APP_BODY></APP_ENV>'
        root = XmlUtils.parse_xml(xml)
        for child in root:
            print(child.tag, child.attrib, root.tag)

    def test_parse_xml_file(self):
        abs_file_path = os.path.join(script_dir, '../../../tests/resources/test.xml' )
        xml = open(abs_file_path, mode='r', encoding='utf-8')
        root = XmlUtils.parse_xml(xml)
        for child in root:
            print(child.tag, child.attrib, root.tag)
        xml.close()

if __name__ == '__main__':
    unittest.main()
