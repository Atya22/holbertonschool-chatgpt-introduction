#!/usr/bin/phyton3

import sys

def factorial(n):
    result = 1
    while n > 1:
		result *= n
		n = n - 1  # Уменьшаем значение n на каждой итерации
	return result

f = factorial(int(sys.argv[1]))
print(f)

