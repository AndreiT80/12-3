# Домашнее задание по теме "Систематизация и пропуск тестов".  suite_12_3.py

import unittest
import test_12_1
import test_12_2
import test_12_3


runTestSuite = unittest.TestSuite()
runTestSuite.addTest(unittest.makeSuite(test_12_1.RunnerTest))
runTestSuite.addTest(unittest.makeSuite(test_12_2.TournamentTest))
runTestSuite.addTest(unittest.makeSuite(test_12_3.TournamentTest))
print("count of tests: " + str(runTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runTestSuite)



# python -m unittest -v test_suite.py