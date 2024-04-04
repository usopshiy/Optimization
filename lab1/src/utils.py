from decimal import *

COLOUMN_SIZE = 9


def print_table_row(row: [Decimal]):
    print(str(row[0]).ljust(COLOUMN_SIZE), end=' | ')
    for i in range(1, len(row)):
        print("{:.2E}".format(row[i]).ljust(COLOUMN_SIZE), end=' | ')
    print()


def print_table_header(row):
    for i in row:
        print(str(i).ljust(COLOUMN_SIZE), end=' | ')
    print("\n" + len(row) * (COLOUMN_SIZE + 3) * "-")


def mid(a, b):
    return Decimal(a + b) / 2


def is_dif_sign(a, b):
    return (a > 0 > b) or (a < 0 < b)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'