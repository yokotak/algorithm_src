# 漢数字とローマ数字の相互変換を行う
# 変換テーブル --- (*1)
KANSUJI = list('零一二三四五六七八九') # 1文字ずつ分解してリストに
ROMASUJI = list('0123456789')

# 変換テーブルを辞書に変換 --- (*2)
KANSUJI_DIC = { key: str(no) for no, key in enumerate(KANSUJI) }
print(KANSUJI_DIC)

# 漢数字に変換 --- (*3)
def to_kansuji(src):
    result = ''
    # 文字列srcを1文字ずつ変換 --- (*3a)
    for c in src:
        if c in ROMASUJI: # リストに変換候補があるか --- (*3b)
            c = KANSUJI[int(c)] # あれば変換 --- (*3c)
        result += c
    return result

# ローマ数字に変換 --- (*4)
def to_romasuji(src):
    result = ''
    # 文字列srcを1文字ずつ変換 --- (*4a)
    for c in src:
        if c in KANSUJI_DIC: # 辞書に変換候補があるか --- (*4b)
            c = KANSUJI_DIC[c] # あれば変換 --- (*4c)
        result += c
    return result

# PyTestで関数をテスト
def test_kansuji():
    assert to_kansuji('345') == '三四五'
    assert to_romasuji('三四五') == '345'

