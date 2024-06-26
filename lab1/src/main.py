import math
from utils import bcolors
from decimal import *
import methods.gold_ratio as gr
import methods.newton as nw
import methods.half_div as hd


def print_answer(x, f):
    print(f"{bcolors.OKBLUE}Ответ:{bcolors.ENDC}\n"
          f"\t {bcolors.OKGREEN}x = {x}\n"
          f"\t f(x) = {f(x)}{bcolors.ENDC}\n")


functions = [[lambda x: Decimal("0.5") * x ** 2 - Decimal.from_float(math.sin(x)),
              lambda x: x - Decimal.from_float(math.cos(x)),
              lambda x: Decimal("1") + Decimal.from_float(math.sin(x))]]
a, b = Decimal("0"), Decimal("1")
max_iter = 11  # variant
accuracy = Decimal("0.0000001")  # variant

if __name__ == "__main__":
    f, deriv1, deriv2 = functions[0][0], functions[0][1], functions[0][2]

    print(f"{bcolors.HEADER}Метод половинного деления{bcolors.ENDC}")
    x = hd.solve(f, a, b, accuracy, max_iter)
    print_answer(x, f)

    print(f"{bcolors.HEADER}Метод золотого сечения{bcolors.ENDC}")
    x = gr.solve(f, a, b, accuracy, max_iter)
    print_answer(x, f)

    print(f"{bcolors.HEADER}Метод ньютона{bcolors.ENDC}")
    x = nw.solve(f, deriv1, deriv2, a, accuracy, max_iter)
    print_answer(x, f)
