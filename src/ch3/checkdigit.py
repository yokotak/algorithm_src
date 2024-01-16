# クレジットカードのチェック --- (*1)
def checkdigit(numbers):
    # 文字列に変換
    numbers = str(numbers)
    # ルーンアルゴリズムで各桁を合計 --- (*2)
    total = 0
    for i, c in enumerate(reversed(numbers)):
        c = int(c)
        # 番号が偶数桁のとき番号を2倍する --- (*3)
        if (i+1) % 2 == 0:
            c = c * 2
            c = c if c < 10 else (c - 9)
        total += c
    # 10で割り切れたら正しい番号 --- (*4)
    return (total % 10 == 0)

# チェックディジットのテスト --- (*5)
def test_checkdigit():
    # 正しい番号のとき
    assert checkdigit('3566002020360505')
    assert checkdigit('4242424242424242')
    assert checkdigit('378282246310005')
    # 間違った番号のとき
    assert checkdigit('000000000000111') == False
    assert checkdigit('00000000000000111') == False

