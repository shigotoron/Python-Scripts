'''
ネイピア数 e の近似値を求めるトリッキーなプログラム
'''

from fractions import Fraction

n = 5
total = 1

for i in reversed(range(1, n)):
    total = 1 + Fraction(total, i)

print(total)
print(float(total))
