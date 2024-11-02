import unittest
from runner import Runner, Tournament


class TournamentTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_turn1(self):
        tour_1 = Tournament(90, self.runner_1, self.runner_3)
        result = tour_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Первый забег'] = result

    def test_turn2(self):
        tour_2 = Tournament(90, self.runner_2, self.runner_3)
        result = tour_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Второй забег'] = result

    def test_turn3(self):
        tour_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tour_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Третий забег'] = result



    if __name__ == '__main__':
        unittest.main()

#  python -m unittest -v test_12_2.py