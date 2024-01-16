# 逆ポーランド記法の計算
def calc_rpn(src):
    # スタックを用意 --- (*1)
    stack = []
    # 文字列をトークンに分割 --- (*2)
    tokens = src.split(' ')
    # トークンを1つずつ処理 --- (*3)
    for t in tokens:
        # 演算子か？ --- (*4)
        if t in '+-*/%':
            b = stack.pop() # スタックから末尾を下ろす
            a = stack.pop() # スタックから末尾を下ろす
            if t == '+': stack.append(a + b) # 計算
            elif t == '-': stack.append(a - b)
            elif t == '*': stack.append(a * b)
            elif t == '/': stack.append(a / b)
            elif t == '%': stack.append(a % b)
        # 数値の場合 --- (*5)
        else:
            stack.append(float(t)) # スタックに数値を載せる
    # スタックに残った値が答え --- (*6)
    return stack.pop()

# 逆ポーランド記法のテスト --- (*7)
def test_rpn():
    assert calc_rpn('2 3 +') == 5
    assert calc_rpn('2 3 * 4 +') == 10
    assert calc_rpn('2 5 3 * +') == 17
    assert calc_rpn('100 2 /') == 50
    assert calc_rpn('30 25 -') == 5

