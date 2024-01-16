import math, sys, re
# 逆ポーランド記法で使う関数を辞書で定義 --- (*1)
RPN_FUNCTIONS = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'ceil': math.ceil,
    'floor': math.floor,
    'round': round,
    'sqrt': math.sqrt,
    'fabs': math.fabs,
    'exp': math.exp,
    'log': math.log,
    'log10': math.log10,
}
# 演算子を辞書で定義 --- (*2)
RPN_OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '%': lambda a, b: a % b
}
# 定数を辞書で定義 --- (*3)
RPN_CONSTANTS = { 'pi': math.pi }

# 逆ポーランド記法の計算 --- (*4)
def calc_rpn(src):
    stack = [] # スタックを用意
    # トークンを区切って一つずつ処理 --- (*5)
    tokens = src.split(' ')
    for t in tokens:
        if t in RPN_FUNCTIONS: # 関数か --- (*6)
            a = stack.pop()
            stack.append(RPN_FUNCTIONS[t](a))
        elif t in RPN_OPERATORS: # 演算子か --- (*7)
            b = stack.pop()
            a = stack.pop()
            stack.append(RPN_OPERATORS[t](a, b))
        elif t in RPN_CONSTANTS: # 定数か --- (*8)
            stack.append(RPN_CONSTANTS[t])
        else:# その他の場合は数値と見なす --- (*9)
            # 数値かどうか正規表現で確認する
            if re.match(r'^([0-9]+|[0-9]+\.[0-9]+)$', t):
                stack.append(float(t))
            else:
                raise ValueError(t+'は数値ではありません')
    return stack.pop() # スタックに残った値が答え

# 逆ポーランド記法のテスト --- (*10)
def test_rpn_func():
    assert calc_rpn('0 sin') == 0
    assert calc_rpn('pi 2 / sin') == 1.0
    assert calc_rpn('pi 3 / cos') == math.cos(math.pi / 3)
    assert calc_rpn('100 sqrt') == math.sqrt(100)
    assert calc_rpn('100 log10') == math.log10(100)
    assert calc_rpn('10 log10') == math.log10(10)
    assert calc_rpn('2 exp') == math.exp(2)

if __name__ == '__main__':
    # コマンドラインを取得 --- (*11)
    if len(sys.argv) <= 1:
        print('[USAGE] rpn_func.py "expr"')
        quit()
    # calc_rpnを呼び出して結果を表示
    print(calc_rpn(sys.argv[1]))

