import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):

    #Test to ensure function works with only two parameters
    def test_city_country(self):
        formatted_city = format_city("Sendai", "Japan")
        self.assertEqual(formatted_city, "Sendai, Japan")

if __name__ == '__main__':
    unittest.main()