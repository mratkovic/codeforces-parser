from argparse import ArgumentParser
import os
import logging
import logging.config


def init_logging():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    logging_conf = os.path.join(dir_path, 'logging_config.ini')
    if not os.path.exists(logging_conf):
        raise FileNotFoundError("Expected logging_config.ini in project root dir")
    logging.config.fileConfig(logging_conf)


def main():
    init_logging()
    parser = ArgumentParser(description='Simple CLI tool for parsing Codeforces contest test samples')
    parser.add_argument('contest', type=int, help='ID of the contest')
    args = parser.parse_args()

    from cfparser import download_cf_contest
    download_cf_contest(args.contest)

if __name__ == '__main__':
    main()
