#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':

    A = tuple(map(int, input().split()))

    if len(A) != 24:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    print("Количество элементов равных пяти: ", A.count(5))
