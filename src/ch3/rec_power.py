# n の m 乗を求める --- (*1)
def power(n, m):
    if m <= 0:
        return 1
    return n * power(n, m - 1)

# テスト --- (*2)
def test_power():
    assert power(2, 2) == 2 ** 2
    assert power(2, 3) == 2 ** 3
    assert power(3, 5) == 3 ** 5

