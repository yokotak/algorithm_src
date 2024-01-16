# ナベアツ問題の答えを返す関数 --- (*1)
def get_nabeatu(num):
    # 3の倍数のとき --- (*2)
    if num % 3 == 0: return 'A'
    # 3が付く数字のとき --- (*3)
    if '3' in str(num): return 'A'
    return str(num) # その他の数字のとき

# get_nabeatuのテスト --- (*4)
def test_get_nabeatu():
    # 3の倍数のとき'A'を出力 --- (*5)
    assert get_nabeatu(3) == 'A'
    assert get_nabeatu(6) == 'A'
    # 3が付く数字のとき'A'を出力 --- (*6)
    assert get_nabeatu(13) == 'A'
    assert get_nabeatu(31) == 'A'
    # それ以外のとき数字を出力 --- (*7)
    assert get_nabeatu(2) == '2'
    assert get_nabeatu(5) == '5'

if __name__ == '__main__':
    # 1から50までの値を出力 --- (*8)
    for i in range(1, 51):
        print(get_nabeatu(i))

