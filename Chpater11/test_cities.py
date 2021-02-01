import unittest
from city_functions import city_function

class TestCityFucntion(unittest.TestCase):
    """ testing a formatted name """
    def test_city_country(self):
        """ do tests like city name , country work """
        test = city_function('chennai', 'india')
        self.assertEqual(test, 'Chennai, India')

    def test_city_country_population(self):
        """ do city, country -populationxxx work? """
        test = city_function('chennai','India',population = 100000)
        self.assertEqual(test, f'Chennai, India - population 100000' )    

if __name__ == '__main__':
    unittest.main()


