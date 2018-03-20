import re
import string
import getpass
import argparse


def load_black_list(path):
    with open(path, 'r') as file_handler:
        black_list = list(file_handler.read().split())
        return black_list


def check_for_black_list(password, black_list):
    if password in black_list:
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
    password_length = len(password)
    if password_length <= 5:
        return -4
    elif password_length > 5 and password_length <= 8:
        return 1
    elif password_length > 10:
        return 4
    else:
        return 2


def check_for_punctuation(password):
    punctuation = string.punctuation
    alpha_list = re.findall(r'.', password)
    if punctuation in alpha_list:
        return 3
    else:
        return 1


def check_password_strength(password, black_list):
    list_strength = list()
    list_strength.append(check_for_black_list(password, black_list))
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
    parser = argparse.ArgumentParser(description='black list with passwords')
    parser.add_argument(
        'path',
        nargs='?',
        default='password.lst',
        help='this is path for black list',
    )
    path = parser.parse_args()
    return path


if __name__ == '__main__':
    try:
        argument = get_parser_args()
        password = getpass.getpass(' input user password: ')
        black_list = load_black_list(argument.path)
        password_strength = (check_password_strength(password, black_list))
        pprint_strength(password_strength)
    except FileNotFoundError:
        print(' ERROR: file "{}" not found'.format(argument.path))
