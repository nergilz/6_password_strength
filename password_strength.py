import re
import string
import getpass
import argparse


def load_bad_list(path):
    with open(path, 'r') as file_handler:
        bad_list = file_handler.read()
        return list(bad_list.split())


def check_for_bad_list(password, dad_list):
    if password in dad_list:
        return -1
    else:
        return 1


def check_for_upper(password):
    if password.isupper():
        return -1
    else:
        return 1


def check_for_digit(password):
    if password.isdigit():
        return -3
    else:
        return 3


def check_for_len(password):
    l = len(password)
    if l <= 5:
        return -4
    elif l > 5 and l <= 8:
        return 1
    elif l > 10:
        return 4
    else:
        return 2


def check_for_punctuation(password):
    punct = string.punctuation
    alpha_list = re.findall(r'.', password)
    if punct in alpha_list:
        return 3
    else:
        return 1


def get_password_strength(password, bad_list):
    list_strength = list()
    list_strength.append(check_for_bad_list(password, bad_list))
    list_strength.append(check_for_upper(password))
    list_strength.append(check_for_digit(password))
    list_strength.append(check_for_len(password))
    list_strength.append(check_for_punctuation(password))
    return sum(list_strength)


def pprint_strength(password_strength):
    if password_strength < 0:
        password_strength = 1
    print(' strength for your password: {}'.format(password_strength))


def get_parser_args():
    parser = argparse.ArgumentParser(description='bad list with passwords')
    parser.add_argument(
        'path',
        nargs='?',
        default='password.lst',
        help='this is path for bad list',
    )
    path = parser.parse_args()
    return path


if __name__ == '__main__':
    try:
        argument = get_parser_args()
        password = getpass.getpass(' input user password: ')
        bad_list = load_bad_list(argument.path)
        password_strength = (get_password_strength(password, bad_list))
        pprint_strength(password_strength)
    except FileNotFoundError:
        print(' ERROR: file "{}" not found'.format(argument.path))
