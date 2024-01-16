# フィボナッチ数列を求める関数
def fib_list(n):
    # 最初は1,1からはじまる --- (*1)
    a, b = 1, 1
    result = [a, b]
    # 繰り返しフィボナッチ数列を求める --- (*2)
    for i in range(1, n-1):
        c = a + b # 次の値を求める --- (*3)
        result.append(c)
        a, b = b, c # aとbの値を更新 --- (*4)
    return result

# テスト
def test_fib_list():
    assert fib_list(3) == [1, 1, 2]
    assert fib_list(8) == [1, 1, 2, 3, 5, 8, 13, 21]

if __name__ == '__main__':
    # フィボナッチ数列を11個表示する --- (*5)
    print(fib_list(11))

