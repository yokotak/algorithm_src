# 10進数から36進数への変換
def dec_to_n36(n):
    disp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while n > 0:
        m = n % 36
        n = n // 36
        result = disp[m] + result
    return result

def test_dec_to_n36():
    assert dec_to_n36(44027) == 'XYZ'
    assert dec_to_n36(37) == '11'


