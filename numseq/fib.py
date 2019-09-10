#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    """Return fibonacci sequence of a number"""
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return b
