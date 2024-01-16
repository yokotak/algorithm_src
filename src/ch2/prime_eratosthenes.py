import math

# エラトステネスのふるいを使って素数を素早く探す
# n以下の素数を全て探す
def get_primes(n):
    result = [] # 素数の結果を入れるリスト
    # 候補リストを初期化(1以前をFalse、2以降をTrue) --- (*1)
    p_list = [False, False] + [True] * (n-2)
    # 繰り返し素数を探す --- (*2)
    sq_n = math.ceil(math.sqrt(n))
    for p in range(2, sq_n):
        if p_list[p]: # 素数を見つけた --- (*3)
            result.append(p)
            # pの倍数を素数候補から外す --- (*4)
            for q in range(p*p, n, p):
                p_list[q] = False
    # 最後までTrueだった要素を素数の結果に追加 --- (*5)
    for i in range(sq_n, n):
        if p_list[i]: result.append(i)
    return result

def test_get_primes():
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert get_primes(50) == answer
    
if __name__ == '__main__':
    print(get_primes(50))
