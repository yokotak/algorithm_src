# データをランレングス圧縮(PickBits)する --- (*1)
def runlength_encode(data):
    result = []
    ch_last = None # 前回の文字
    ch_count = 0 # 繰り返し回数
    discont_chars = [] # 非連続の文字
    # データを1つずつ確認する --- (*2)
    for ch in data + '\0':
        # 前回と同じ文字が連続している場合 --- (*3)
        if ch_last == ch:
            ch_count += 1
            out_discont(discont_chars, result) # 非連続文字を出力
            continue
        # 前回と異なる文字のとき --- (*4)
        if ch_count > 0:
            if ch_count == 1: # 1回だけなら非連続文字に追加
                discont_chars.append(ch_last)
            else:
                result.append(str(ch_count)) # 回数を出力
                result.append(ch_last) # 文字を出力
        ch_last = ch # 今回の文字 --- (*5)
        ch_count = 1 # 繰り返し回数を初期化
    out_discont(discont_chars, result)
    return ''.join(result)

# 非連続文字があれば出力 --- (*6)
def out_discont(discont_chars, result):
    if len(discont_chars) > 0:
        result.append(str(-1 * len(discont_chars)))
        for ch in discont_chars:
            result.append(ch)
        discont_chars.clear()

# テスト --- (*7)
def test_runlength_encode():
    assert runlength_encode('AAAbcDDDDD') == '3A-2bc5D'
    assert runlength_encode('AAABBBBCCCCC') == '3A4B5C'
    assert runlength_encode('AAAAAAAAAAAAAAAbc') == '15A-2bc'

if __name__ == '__main__':
    print(runlength_encode('AAAbcDDDDD'))
