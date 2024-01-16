# PyTestを使って偶数判定を行う関数 --- (*1)
def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(5) == False

# 偶数かどうか判定する関数 --- (*2)
def is_even(num):
    return (num % 2 == 0)


