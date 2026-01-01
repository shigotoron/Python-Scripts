'''
F_0 から F_{n - 1} までの n 個のフィボナッチ数を計算して表示するプログラム
'''

n = 10

F = [0] * n
F[0] = 0
F[1] = 1

for k in range(n - 2):
    F[k + 2] = F[k + 1] + F[k]

for k in range(n):
    print("F_" + str(k) + " = " + str(F[k]))
