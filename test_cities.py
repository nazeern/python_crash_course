import unittest
from city_functions import get_city_country

class CityFunctionsTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_country_city(self):
        result = get_city_country('kerala', 'india')
        self.assertEqual(result, 'Kerala, India')

    def test_country_city_population(self):
        string = get_city_country('kerala', 'india', 100000)
        expected_string = 'Kerala, India: Population -- 100000'
        self.assertEqual(string, expected_string)

unittest.main()
