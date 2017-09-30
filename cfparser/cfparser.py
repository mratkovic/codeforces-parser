from bs4 import BeautifulSoup
import requests

CONTEST_URL_SCHEME = 'http://codeforces.com/contest/{contest}'
PROBLEM_URL_SCHEME = 'http://codeforces.com/contest/{contest}/problem/{problem}'


def parse_contest_for_problem_list(contest_id):
    url = CONTEST_URL_SCHEME.format(contest=contest_id)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    problems_table = soup.findAll('table', 'problems')
    if len(problems_table) != 1:
        # expected single problems table
        return None

    html_problems_list = problems_table[0].findAll('td', 'id')
    return [x.get_text().strip() for x in html_problems_list]


def parse_problem(contest_id, problem_id):
    url = PROBLEM_URL_SCHEME.format(contest=contest_id, problem=problem_id)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for br in soup.find_all('br'):
        br.replace_with('\n')

    tests = soup.findAll('div', 'sample-test')
    if len(tests) != 1:
        # expected single sample-tests div
        return None
    tests = tests[0]

    def get_sample_data(bs_divs):
        return [x.pre.get_text() for x in bs_divs]

    ins = get_sample_data(tests.findAll('div', 'input'))
    outs = get_sample_data(tests.findAll('div', 'output'))
    return zip(ins, outs)
