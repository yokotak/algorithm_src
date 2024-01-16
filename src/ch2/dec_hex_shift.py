# ビットシフトで10進数を16進数に変換する関数 
def dec_to_hex(n):
    label = '0123456789ABCDEF'
    result = ''
    if n == 0:
        return '0'
    while n > 0:
        m = n & 0b1111 # 今回の桁を求める --- (*1)
        n = n >> 4     # 次回の値
        result = label[m] + result # 今回の桁を文字列で追加
    return result

def test_dec_to_hex():
    assert dec_to_hex(255) == 'FF'
    assert dec_to_hex(256) == '100'
    assert dec_to_hex(0) == '0'


