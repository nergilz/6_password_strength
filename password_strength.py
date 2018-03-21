import re
import getpass
import argparse


def load_black_list(path):
    with open(path, 'r') as file_handler:
        black_list = list(file_handler.read().splitlines())
        return black_list


def is_psw_in_black_list(password, black_list):
    return -1 if password in black_list else 1


def has_upper(password):
    return -1 if password.isupper() else 1


def has_digit(password):
    return -3 if password.isdigit() else 3


def length_check(password):
    password_length = len(password)
    min_len = 5
    middle_len = 8
    max_len = 10
    return -4 if password_length <= min_len \
        else 1 if password_length > min_len and password_length <= middle_len \
        else 3 if password_length > max_len else 2


def is_punctuation_in_psw(password):
    return 2 if re.search(r'\W', password) else 1


def get_password_strength(password, black_list):
    return sum([
        is_psw_in_black_list(password, black_list),
        has_upper(password),
        has_digit(password),
        length_check(password),
        is_punctuation_in_psw(password)
        ])


def pprint_strength(password_strength):
    print(' strength your password: {}'.format(max([password_strength, 1])))


def get_parser_args():
    parser = argparse.ArgumentParser(description='black list with passwords')
    parser.add_argument(
        'path',
        nargs='?',
        default='password.lst',
        help='this is path for black list',
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    try:
        arguments = get_parser_args()
        password = getpass.getpass(' input user password: ')
        black_list = load_black_list(arguments.path)
        password_strength = (get_password_strength(password, black_list))
        pprint_strength(password_strength)
    except FileNotFoundError:
        print(' ERROR: file "{}" not found'.format(arguments.path))
