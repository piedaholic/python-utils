import unittest
from root_utils import *

class TestRootUtils(unittest.TestCase):

    def test_nvl_str(self):
        a = ''
        assert nvl(a,'Harsh') == 'Harsh'
        a = str()
        assert nvl(a,'Harsh') == 'Harsh'
        a = None
        assert nvl(a,'Harsh') == 'Harsh'
        assert nvl('XYZ','Harsh') == 'XYZ'


if __name__ == '__main__':
    unittest.main()
