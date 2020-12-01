from one_hot import fit_transform
import unittest


class Test_one_hot(unittest.TestCase):

    def test_base(self):
        """
        Проверка на равенство полученных значений с ожидаемым выводом функции
        """
        capitals = ['Moscow', 'New York', 'Moscow', 'London']
        transformed_cities = fit_transform(capitals)
        exp_transformed_cities = [('Moscow', [0, 0, 1]),
                                  ('New York', [0, 1, 0]),
                                  ('Moscow', [0, 0, 1]),
                                  ('London', [1, 0, 0])]
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_weather(self):
        """
        Проверка на неравенство полученных значений с ожидаемым выводом функции
        """
        words = ['cold', 'cold', 'warm', 'cold', 'warm', 'hot']
        transformed_words = fit_transform(words)
        exp_str = [('cold', [0, 0, 1]),
                   ('cold', [0, 0, 1]),
                   ('warm', [1, 1, 0]),
                   ('hot', [1, 0, 0])]
        self.assertNotEqual(transformed_words, exp_str)

    def test_exception(self):
        """
        Проверка на исключение функции без параметров
        """
        with self.assertRaises(TypeError):
            fit_transform()

    def test_integer(self):
        """
        Проверка на исключение функции, получающей на вход цифру
        """
        number = 2
        with self.assertRaises(TypeError):
            fit_transform(number)

    def test_not_none(self):
        """
        Проверка вывода функции не None значения
        """
        cities = ['Moscow', 'Kiev']
        self.assertIsNotNone(fit_transform(cities))

    def test_empty(self):
        """
        Проверка вывода функции, получающей на вход пустой список
        """
        city = []
        self.assertEqual(fit_transform(city), [])


if __name__ == '__main__':
    unittest.main()
