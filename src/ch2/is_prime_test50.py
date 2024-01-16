# 関数is_primeを網羅的にテストする関数
def test_is_prime_all():
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_list = []
    for i in range(1, 51): # 50以下の値を全て試す
        if is_prime(i):
            prime_list.append(i)
    assert prime_list == answer # 答え合わせ

# 試し割り法でnが素数か確認する関数
def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True
