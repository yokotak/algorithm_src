# 漢数字とローマ数字の相互変換を行う
# 変換テーブル --- (*1)
KANSUJI = list('零一二三四五六七八九') # 1文字ずつ分解してリストに
ROMASUJI = '0123456789'
# 変換テーブルを辞書に変換 --- (*2)
KANSUJI_DIC = {}
for i, c in enumerate(KANSUJI):
    KANSUJI_DIC[c] = str(i)

# 漢数字に変換 --- (*3)
def to_kansuji(src):
    result = ''
    for c in src:
        if c in ROMASUJI:
            c = KANSUJI[int(c)]
        result += c
    return result

# ローマ数字に変換 --- (*4)
def to_romasuji(src):
    conv_f = lambda c: KANSUJI_DIC[c] if c in KANSUJI_DIC else c
    converted = map(conv_f, list(src))
    return ''.join(converted)

'''
def to_romasuji(src):
    result = ''
    for c in src:
        if c in KANSUJI_DIC:
            c = KANSUJI_DIC[c]
        result += c
    return result
'''

# PyTestで関数をテスト
def test_kansuji():
    assert to_kansuji('345') == '三四五'
    assert to_romasuji('三四五') == '345'

