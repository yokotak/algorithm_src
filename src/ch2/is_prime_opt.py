import math

# 最適化した試し割り法で素数かどうかを判定する関数
def is_prime(n):
    # 2未満の値は素数ではない
    if n < 2: return False
    # 2は素数である --- (*1)
    if n == 2: return True
    # 2の倍数は素数ではない --- (*2)
    if n % 2 == 0: return False
    # 素数判定のためには、nの平方根までを割れば良い --- (*3)
    sq = math.ceil(math.sqrt(n))
    # 3からsqまで偶数を飛ばして割り切れるかを試す --- (*4)
    for i in range(3, sq+1, 2):
        if n % i == 0: return False
    return True

# 関数is_primeを網羅的にテストする関数 --- (*5)
def test_is_prime_all():
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_list = list(filter(is_prime, range(1, 51)))
    assert prime_list == answer

print(is_prime(50))