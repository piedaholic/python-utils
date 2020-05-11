import unittest

class TestFileUtils(unittest.TestCase):
      work_dir=str()

      def __init__(self):
          print('Here')
          if TestFileUtils.work_dir != '':
              TestFileUtils.work_dir = 'D:\\Temp\\MyLogs'
          print(TestFileUtils.work_dir)
          self.fu = FileUtils()

      def read_file(self):
          filename = 'demo_file'
          self.fu.create_text_file(fu.join_path(TestFileUtils.work_dir, filename))

if __name__ == '__main__':
    unittest.main()
