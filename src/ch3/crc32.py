import binascii
# CRC-32を計算するのに必要な定数
CRC32POLY = 0xEDB88320

# CRC-32を計算する関数 --- (*1)
def crc32(bin_data):
    crc = 0xffffffff # 初期値
    for b in bin_data: # 1バイトずつ繰り返す --- (*2)
        crc ^= b # XOR演算 --- (*3)
        for bit in range(8): # 8回(8ビット分)繰り返す --- (*4)
            if (crc & 1) == 1: # 下位ビットが1か？ --- (*5)
                crc >>= 1
                crc ^= CRC32POLY # XOR
            else:
                crc >>= 1
    return crc ^ 0xffffffff # ビットを反転 --- (*6)

# CRC-32のテスト --- (*7)
def test_crc32():
    assert crc32(b'hello') == binascii.crc32(b'hello')
    assert crc32(b'world') == binascii.crc32(b'world')
    assert crc32(b'abcd') == binascii.crc32(b'abcd')
    assert crc32(b'test') == 0xD87F7E0C
    assert crc32(b'hoge') == 0x8B39E45A 
