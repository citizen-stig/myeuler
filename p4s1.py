# -*- encoding: utf-8 -*-
"""
A palindromic number reads the same both ways.The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def get_number():
    max_n = 0
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            n = i * j
            n_s = str(n)
            if n_s == n_s[::-1] and n > max_n:
                max_n = n
    return max_n

print(get_number())


