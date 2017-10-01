import unittest
import logging
import shutil
import tempfile
import os
import cfparser.cfparser as cf


class CFFilesTests(unittest.TestCase):

    def setUp(self):
        # suppress all log messages during tests
        logging.disable(logging.ERROR)

        # make tmp dir
        self.tmp_root = tempfile.mkdtemp()

    def tearDown(self):
        # restore logging rules
        logging.disable(logging.NOTSET)
        shutil.rmtree(self.tmp_root)

    def generic_test(self, contest, problem_list, n_test_samples_list):
        cf.download_cf_contest(contest, self.tmp_root)
        contest_dir = os.path.join(self.tmp_root, str(contest))
        self.assertTrue(os.path.exists(contest_dir))
        self.assertTrue(os.path.isdir(contest_dir))

        for subproblem, n_tests in zip(problem_list, n_test_samples_list):
            subdir = os.path.join(contest_dir, subproblem)
            self.assertTrue(os.path.exists(subdir))
            self.assertTrue(os.path.isdir(subdir))

            tests_dir = os.path.join(subdir, cf.TESTS_SUBDIR)
            self.assertTrue(os.path.exists(tests_dir))
            self.assertTrue(os.path.isdir(tests_dir))

            tests = os.listdir(tests_dir)
            self.assertEqual(len(tests), 2*n_tests)

    def test_dumped_tests1(self):
        self.generic_test(1, ['A', 'B', 'C'], [1, 1, 1])

    def test_dumped_tests2(self):
        self.generic_test(100,
                          list('ABCDEFGHIJ'),
                          [2, 2, 3, 2, 2, 2, 2, 1, 2, 2])

if __name__ == '__main__':
    unittest.main()
