#!/usr/bin/env python3

import sys

"""
Executed as LD.so
"""

if __name__ == "__main__":
    head = sys.stdin.read(64)
    print(head)
