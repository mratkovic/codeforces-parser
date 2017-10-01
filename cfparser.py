import logging
import os

import requests
from argparse import ArgumentParser
from bs4 import BeautifulSoup

# define logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# URL schemes
CONTEST_URL_SCHEME = 'http://codeforces.com/contest/{contest}'
PROBLEM_URL_SCHEME = 'http://codeforces.com/contest/{contest}/problem/{problem}'

# Test location and naming definition
TESTS_SUBDIR = 'tests'
IN_FILE_PATTERN = 'test.in.{id}'
OUT_FILE_PATTERN = 'test.out.{id}'


def parse_contest_for_problem_list(contest_id):
    """
    Parses codeforces contest page for list of problems.

    Parameters
    ----------
    contest_id : int
        id of codeforces contest, can be seen in the url, example codeforces.com/contest/100/

    Returns
    -------
    problem_list : list of strings
        list of problem names, example ['A', 'B', ...]
    """
    logger.debug('Parsing problem %s', contest_id)
    url = CONTEST_URL_SCHEME.format(contest=contest_id)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    problems_table = soup.findAll('table', 'problems')
    if len(problems_table) != 1:
        logger.warning('Contest %s page parsing failed. Problems table not found', contest_id)
        return []

    html_problems_list = problems_table[0].findAll('td', 'id')
    problem_list = [x.get_text().strip() for x in html_problems_list]
    logger.debug('Parsed contest page, found %s problems %s', len(problem_list), problem_list)
    return problem_list


def parse_problem(contest_id, problem_id):
    """
    Parses codeforces problem page for provided test samples.


    Parameters
    ----------
    contest_id : int
        id of codeforces contest, can be seen in the url, example codeforces.com/contest/100/
    problem_id : str
        name of codeforces problem, can be seen in the url, example codeforces.com/contest/100/problem/A/

    Returns
    -------
    tests : zip object
        zip object of pairs of strings (input, output)

    """
    logger.debug('Parsing problem %s', problem_id)
    url = PROBLEM_URL_SCHEME.format(contest=contest_id, problem=problem_id)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for br in soup.find_all('br'):
        br.replace_with('\n')

    tests = soup.findAll('div', 'sample-test')
    if len(tests) != 1:
        logger.warning('Contest %s, problem %s page parsing failed. Tests not found', contest_id, problem_id)
        return []

    def get_sample_data(bs_divs):
        return [x.pre.get_text() for x in bs_divs]

    tests = tests[0]
    ins = get_sample_data(tests.findAll('div', 'input'))
    outs = get_sample_data(tests.findAll('div', 'output'))
    logger.debug('Parsed problem %s, found %s test samples', problem_id, len(ins))
    return zip(ins, outs)


def dump_tests_to_file(contest, problem, tests, root='./'):
    """
    Dumps parsed tests to files.

    In given `root` creates dir for contest with subdirs for every problem that contain tests directory. Test samples
    are stored in the tests subdirectory.

    Parameters
    ----------
    contest : int
        id of codeforces contest, can be seen in the url, example codeforces.com/contest/100/
    problem : str
        name of codeforces problem, can be seen in the url, example codeforces.com/contest/100/problem/A/
    tests : zip
        zip object of pairs of strings (input, output)
    root : str
        root dir where tests where file structure will be created
    """
    if not tests:
        return []

    tests_path = os.path.join(root, str(contest), problem, TESTS_SUBDIR)
    #os.makedirs(tests_path, exist_ok=True)
    # added for support with py2
    try:
        os.makedirs(tests_path)
    except OSError:
        pass

    def dump_to_file(data, file_path):
        with open(file_path, 'w') as fout:
            fout.write(data)

    for i, (in_data, out_data) in enumerate(tests):
        in_path = os.path.join(tests_path, IN_FILE_PATTERN.format(id=i))
        out_path = os.path.join(tests_path, OUT_FILE_PATTERN.format(id=i))

        dump_to_file(in_data, in_path)
        dump_to_file(out_data, out_path)


def download_cf_contest(contest, root_path='./'):
    """
    Parses codeforces contest and downloads test data for all the problems.

    Following file structure is created in provided `root_path`:
        <root_path>/<contest>/<problem>/tests/

    Parameters
    ----------
    contest : int
        id of codeforces contest, can be seen in the url, example codeforces.com/contest/100/
    root_path : str
        root dir where tests where file structure will be created
    """
    logger.info('Parsing contest %s', contest)
    problem_list = parse_contest_for_problem_list(contest)

    for problem in problem_list:
        logger.info('Parsing problem %s', problem)
        tests_data = parse_problem(contest, problem)
        dump_tests_to_file(contest, problem, tests_data, root_path)


def main():
    parser = ArgumentParser(description='Simple CLI tool for parsing Codeforces contest test samples')
    parser.add_argument('contest', type=int, help='ID of the contest')
    parser.add_argument('root_dir', type=str, default='./', nargs='?',
                        help='Optional argument root dir, where file structure will be created. '
                             'By default, this is current dir')
    args = parser.parse_args()
    download_cf_contest(args.contest, args.root_dir)

if __name__ == '__main__':
    main()
