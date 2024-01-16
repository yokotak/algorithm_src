# ランレングス圧縮した文字列を展開する --- (*1)
def runlength_decode(data):
    result = ''
    nums = ''
    counter = 0 # 繰り返す回数
    # 1文字ずつ処理する --- (*2)
    for ch in data:
        # 回数が0の時に回数を読む --- (*3)
        if counter == 0:
            if ch in '-0123456789':
                nums += ch
                continue
            # 繰り返し回数を得る --- (*4)
            counter = int(nums)
            nums = ''
        # 繰り返し回数だけ文字を結果に追加 --- (*5)
        if counter > 0:
            result += ch * counter
            counter = 0
        # 非連続文字があるか？ --- (*6)
        if counter < 0:
            result += ch
            counter += 1
    return result

# テスト --- (*7)
def test_runlength_decode():
    assert runlength_decode('3A-2bc3D') == 'AAAbcDDD'
    assert runlength_decode('3A4B5C') == 'AAABBBBCCCCC'
    assert runlength_decode('15A-2bc') == 'AAAAAAAAAAAAAAAbc'
    assert runlength_decode('-4test5!') == 'test!!!!!'

if __name__ == '__main__':
    print(runlength_decode('3A-2bc3D'))
