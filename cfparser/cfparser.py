import requests
import os
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

CONTEST_URL_SCHEME = 'http://codeforces.com/contest/{contest}'
PROBLEM_URL_SCHEME = 'http://codeforces.com/contest/{contest}/problem/{problem}'

TESTS_SUBDIR = 'tests'

IN_FILE_PATTERN = 'test.in.{id}'
OUT_FILE_PATTERN = 'test.out.{id}'


def parse_contest_for_problem_list(contest_id):
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
    if not tests:
        return []

    tests_path = os.path.join(root, str(contest), problem, TESTS_SUBDIR)
    os.makedirs(tests_path, exist_ok=True)

    def dump_to_file(data, file_path):
        with open(file_path, 'w') as fout:
            fout.write(data)

    for i, (in_data, out_data) in enumerate(tests):
        in_path = os.path.join(tests_path, IN_FILE_PATTERN.format(id=i))
        out_path = os.path.join(tests_path, OUT_FILE_PATTERN.format(id=i))

        dump_to_file(in_data, in_path)
        dump_to_file(out_data, out_path)


def download_cf_contest(contest, root_path='./'):
    logger.info('Parsing contest %s', contest)
    problem_list = parse_contest_for_problem_list(contest)

    for problem in problem_list:
        logger.info('Parsing problem %s', problem)
        tests_data = parse_problem(contest, problem)
        dump_tests_to_file(contest, problem, tests_data, root_path)


