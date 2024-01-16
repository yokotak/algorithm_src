# 10進数から8進数に変換 --- (*1)
def dec_to_oct(n):
    result = ''
    while n > 0:
        m = n % 8 # --- (*2)
        n = n // 8
        result = str(m) + result
    return result

# 8進数から10進数に変換 --- (*3)
def oct_to_dec(oct_str):
    result = 0
    for c in oct_str:
        result *= 8
        result += int(c) if c in '01234567' else 0
    return result

# テスト --- (*4)
def test_oct_dec():
    assert dec_to_oct(8) == '10'
    assert dec_to_oct(10) == '12'
    assert oct_to_dec('10') == 8
    assert oct_to_dec('12') == 10


