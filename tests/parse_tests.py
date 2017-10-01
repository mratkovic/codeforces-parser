import unittest
import logging
import cfparser as cf


class CFParseTests(unittest.TestCase):

    def setUp(self):
        # suppress all log messages during tests
        logging.disable(logging.ERROR)

    def tearDown(self):
        # restore logging rules
        logging.disable(logging.NOTSET)

    def test_parse_contest_n_problems1(self):
        problems = cf.parse_contest_for_problem_list(1)
        self.assertEqual(len(problems), 3)

    def test_parse_contest_problems1(self):
        problems = cf.parse_contest_for_problem_list(1)
        self.assertEqual(problems, ['A', 'B', 'C'])

    def test_parse_contest_n_problems2(self):
        problems = cf.parse_contest_for_problem_list(100)
        self.assertEqual(len(problems), 10)

    def test_parse_contest_problems2(self):
        problems = cf.parse_contest_for_problem_list(100)
        expected_problems = map(chr, range(ord('A'), ord('J') + 1))
        self.assertEqual(problems, list(expected_problems))

    def test_parse_invalid_contest(self):
        problems = cf.parse_contest_for_problem_list(-2)
        self.assertEqual(problems, [])

    def test_parse_n_test1(self):
        tests = list(cf.parse_problem(1, 'A'))
        self.assertEqual(len(tests), 1)

    def test_parse_n_test2(self):
        tests = list(cf.parse_problem(100, 'A'))
        self.assertEqual(len(tests), 2)

    def test_parse_n_test1(self):
        tests = list(cf.parse_problem(1, 'Z'))
        self.assertEqual(tests, [])

    def test_parse_tests1(self):
        tests = list(cf.parse_problem(1, 'A'))
        self.assertEqual(len(tests), 1)

        input_data, output_data = tests[0]
        self.assertEqual(input_data.strip(), '6 6 4')
        self.assertEqual(output_data.strip(), '4')

    def test_parse_tests2(self):
        tests = list(cf.parse_problem(1, 'C'))
        self.assertEqual(len(tests), 1)

        input_data, output_data = tests[0]
        self.assertEqual(input_data.strip(),
                          '0.000000 0.000000\n1.000000 1.000000\n0.000000 1.000000')
        self.assertEqual(output_data.strip(), '1.00000000')

    def test_parse_tests3(self):
        tests = list(cf.parse_problem(100, 'C'))
        self.assertEqual(len(tests), 3)

        input_data, output_data = tests[0]
        self.assertEqual(input_data.strip(), '2\n3')
        self.assertEqual(output_data.strip(), '5')

        input_data, output_data = tests[1]
        self.assertEqual(input_data.strip(), '1390\n2011')
        self.assertEqual(output_data.strip(), '3401')

        input_data, output_data = tests[2]
        self.assertEqual(input_data.strip(), '12345\n54321')
        self.assertEqual(output_data.strip(), '66666')

if __name__ == '__main__':
    unittest.main()
