'''
素数判定する関数のテスト
>>> list(filter(is_prime, range(1, 51)))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''

# 素数かどうかを判定する関数
def is_prime(n):
    # 2未満の値は素数ではない
    if n < 2: return False
    # 2からn-1まで順に割り切れるかどうかを試す
    for i in range(2, n):
        if n % i == 0: return False
    return True

