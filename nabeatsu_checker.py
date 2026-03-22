'''
世界のナベアツさんがアホになる回数をカウントします
'''

n = 2026
count = 0

def is_nabeatsu_number(a):
    return a % 3 == 0 or ('3' in str(a))
    
for k in range(1, n + 1):
    if is_nabeatsu_number(k):
        count += 1

print("世界のナベアツさんが 1 から", n, "まで数えるとき, 彼がアホになる回数は", count, "回です。")
