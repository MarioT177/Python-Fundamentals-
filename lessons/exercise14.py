# 1  11-1: City,Country:

import unittest

from city_func import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        wichita_usa = city_country('wichita', 'usa')
        self.assertEqual(wichita_usa, 'Wichita, Usa')

if __name__ == '__main__':
    unittest.main()


# 2 11-2: population:

import unittest

from city_func import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        wichita_usa = city_country('wichita', 'usa')
        self.assertEqual(wichita_usa, 'Wichita, Usa')

    def test_city_country_population(self):
        wichita_usa = city_country('wichita', 'usa', population=300_000)
        self.assertEqual(wichita_usa, 'Wichita, Usa - population 300000')

if __name__ == '__main__':
    unittest.main()

# 3 11-3 Employee:

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.mario = Employee('mario', 'trujillo', 40_000)

    def test_give_default_raise(self):
        self.mario.give_raise()
        self.assertEqual(self.mario.salary, 45000)

    def test_give_custom_raise(self):
        self.mario.give_raise(10000)
        self.assertEqual(self.mario.salary, 50000)

if __name__ == '__main__':
    unittest.main()

