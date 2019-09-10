#!/usr/bin/env python
# -*- coding: utf-8 -*-


def primes(n):
    """Going over a range of the passed in number,
    and returning the prime numbers"""
    list = []
    for num in range(n):
        if is_prime(num):
            list.append(num)
    return list


def is_prime(n):
    """Checking if the passed in number is prime with a boolean"""
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
