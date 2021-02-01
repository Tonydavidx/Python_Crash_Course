import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """ test for name_function.py """

    def test_first_last_name(self):
        """ do names like Leonardo David work? """
        formatted_name = get_formatted_name('tony','david')
        self.assertEqual(formatted_name, 'Tony David')

if __name__ == '__main__':
    unittest.main()        