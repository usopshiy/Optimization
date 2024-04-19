from utils import *


def solve(f, deriv, deriv2, start, accuracy, max_iter):
    def find_x():
        return x - deriv(x) / deriv2(x)

    iter = 1
    x, prev_x = start, start
    x = find_x()
    print_table_header(["#", "x_i", "f(x)", "f'(x)"])
    print_newton_row([iter, prev_x, f(x), deriv(x)])
    while abs(deriv(x)) > accuracy and iter < max_iter:
        iter += 1
        prev_x = x
        x = find_x()
        print_newton_row([iter, prev_x, f(x), deriv(x)])
    return x
