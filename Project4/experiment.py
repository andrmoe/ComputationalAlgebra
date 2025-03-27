from random_squares import random_squares_factoring
from quadratic_sieve import quadratic_sieve_factoring
from examples_brillhart_and_selfridge import factorizations


def experiment():
    for expression in factorizations.keys():
        expression = expression.replace('^', '**')
        N = eval(expression)
        print(expression, '=', N)
        factor = quadratic_sieve_factoring(N)
        print(factor, N % factor)



if __name__ == '__main__':
    experiment()