from utils import *


def solve(f, a, b, accuracy, max_iter):
    iter = 0
    print_table_header(["#", "a", "b"])
    while abs(a - b) > 2 * accuracy and iter < max_iter:
        iter += 1
        x1 = mid(a, b - accuracy)
        x2 = mid(a, b + accuracy)
        if f(x1) > f(x2):
            a = x1
        else:
            b = x2
        print_table_row([iter, a, b])
    x = mid(a, b)
    return x
