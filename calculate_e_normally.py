'''
ネイピア数 e の近似値を普通に求めるプログラム
'''

from fractions import Fraction
import math

n = 10
total = 0

for i in range(n):
    total += Fraction(1, math.factorial(i))

print(total)
print(float(total))
