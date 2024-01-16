# 素数かどうかを判定する関数 --- (*1)
def is_prime(n):
    if n < 2: return False
    # 順にn-1の値で割り切れるか試す
    for i in range(2, n):
        if n % i == 0: return False
    return True

# 値をカンマで区切り10個ずつ改行して返す
def get_prime_game(max_value):
    res = ''
    # 1からmax_valueまで繰り返す --- (*2)
    for n in range(1, max_value+1):
        # 素数ならPを、素数でなければ数値を返す --- (*3)
        if is_prime(n):
            v = 'P'
        else:
            v = n
        res += '{:>4}'.format(v)
        # 値をカンマで区切り10個ずつ改行を出力 --- (*4)
        if (n-1) % 10 == 9:
            res += '\n'
        else:
            res += ','
    return res

if __name__ == '__main__':
    # 1から200までの値を順に出力 --- (*5)
    print(get_prime_game(200))
