# 別ファイル「is_prime.py」にある関数「is_prime」を取り込む
from is_prime import is_prime

# 関数is_primeを網羅的にテストする関数
def test_is_prime_all():
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_list = list(filter(is_prime, range(1, 51)))
    assert prime_list == answer
