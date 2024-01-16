# 10進数から2進数に変換 --- (*1)
def dec_to_bin(n):
    result = ''
    while n > 0:
        m = n & 1 # 2進数の末尾1桁を取り出す --- (*2)
        n = n >> 1 # ビットを1桁右にずらす
        result = ('0' if m == 0 else '1') + result
    return result

# 2進数から10進数に変換 --- (*3)
def bin_to_dec(bin_str):
    result = 0
    for c in bin_str:
        result = result << 1 # 桁を1つ左にずらす --- (*4)
        result += 1 if c == '1' else 0
    return result

# テスト --- (*5)
def test_dec_bin():
    assert dec_to_bin(3) == '11'
    assert dec_to_bin(15) == '1111'
    assert dec_to_bin(5) == '101'
    assert bin_to_dec('11111111') == 255
    assert bin_to_dec('101') == 5

if __name__ == '__main__':
    print('dec_to_bin(5)    =>', dec_to_bin(5))
    print('bin_to_dec("101") =>', bin_to_dec('101'))

