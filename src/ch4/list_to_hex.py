# 数値リストをHEX文字列に変換する関数 --- (*1)
def list_to_hex(a_list):
    return ''.join(map(lambda v: f'{v:02x}', a_list))

# テスト --- (*2)
def test_bin_to_hex():
    assert list_to_hex([0xFF, 0x07, 0x40]) == 'ff0740'
    assert list_to_hex([0x1, 0x2, 0x3]) == '010203'
    assert list_to_hex([]) == ''
    assert list_to_hex([0xFF, 0xEE, 0x33, 0x22]) == 'ffee3322'


