# 引数nが素数かどうかを調べる関数(完成版)
def is_prime(n):
    # 2未満の値は素数ではない --- (*1)
    if n < 2:
        return False
    # 2からn-1まで順に割り切れるかどうかを試す --- (*2)
    for i in range(2, n):
        if n % i == 0: # 割り切れるか？
            return False
    # 割り切れなかったので素数である --- (*3)
    return True

# 関数is_primeをテストする関数 --- (*4)
def test_is_prime():
    assert is_prime(3) == True
    assert is_prime(8) == False
    assert is_prime(89) == True

