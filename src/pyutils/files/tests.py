import unittest
from file_utils import FileUtils

class TestFileUtils(unittest.TestCase):

    def setUp(self):
        self.work_dir = 'D:\\Temp\\MyLogs'
        self.fu = FileUtils()
        self.filename = 'demo_file.log'
        self.file = self.fu.join_path(self.work_dir, self.filename)
        self.dirname = 'demo'
        self.dir = self.fu.join_path(self.work_dir, self.dirname)

    def test_file(self):
        text = 'Hello World!'
        FileUtils.create_text_file(self.file)
        FileUtils.write_to_file(self.file,text)
        assert FileUtils.read_file(self.file) == text
        FileUtils.remove_file(self.file)

    def test_directory(self):
        FileUtils.create_directory(self.dir)
        assert FileUtils.exists(self.dir)
        FileUtils.remove_directory(self.dir)

if __name__ == '__main__':
    unittest.main()
