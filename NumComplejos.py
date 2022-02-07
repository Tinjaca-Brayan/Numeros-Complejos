# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math


def sumacplx(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1])


if __name__ == '__main__':
    print(sumacplx((3.5, 7), (4.2, 8)))


def multiplicacion(c1, c2):
    real = (c1[0] * c2[0]) - (c1[1] * c2[1])
    imaginario = (c1[0] * c2[1]) + (c1[1] * c2[0])
    return (real, imaginario)


if __name__ == '__main__':
    print(multiplicacion((3, 7), (4, 8)))


def resta(c1, c2):
    return (c1[0] - c2[0], c1[1] - c2[1])


if __name__ == '__main__':
    print(resta((3.5, 7), (4.2, 8)))


def division(c1, c2):
    real = ((c1[0] * c2[0]) + (c1[1] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    imaginario = ((c2[0] * c1[1]) - (c1[0] * c2[1])) / ((c2[0] ** 2) + (c2[1] ** 2))
    return (real, imaginario)


if __name__ == '__main__':
    print(division((3, 2), (4, -5)))


def modulo(c1):
    return (((c1[0] ** 2) + (c1[1] ** 2)) ** 0.5)


if __name__ == '__main__':
    print(modulo((5, 7)))


def conjugado(c1):
    return ((c1[0], -c1[1]))


if __name__ == '__main__':
    print(conjugado((5, 7)))


def conversor(c1):
    grados = math.atan(c1[1] / c1[0])
    return ((modulo(c1)), ((grados * 180 / 3.1416) / 180))


if __name__ == '__main__':
    print("radio:", conversor((3, -4)), "pi radianes")


def fase(c1):
    return (math.atan(c1[1] / c1[0]) * 180 / 3.1416)


if __name__ == '__main__':
    print(fase((3, -4)), "grados")





