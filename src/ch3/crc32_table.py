import binascii
# CRC-32を計算するためのテーブル
crc32_table = []
# CRC-32の計算用テーブルを初期化 --- (*1)
def crc32_get_table():
    # 既にテーブルがあれば作成済みのものを返す
    if len(crc32_table) != 0:
        return crc32_table
    # 0から255まで256個の値を生成
    for byte in range(256):
        crc = 0
        for bit in range (8):
            if (byte ^ crc) & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
            byte >>= 1
        crc32_table.append(crc)
    return crc32_table

# テーブルを使ってCRC-32を求める --- (*2)
def crc32(bin_data):
    table = crc32_get_table()
    crc = 0xffffffff
    # テーブルを活用してCRCを計算 --- (*3)
    for b in bin_data:
        crc = table[(crc & 0xFF) ^ b] ^ (crc >> 8)
    return 0xffffffff ^ crc

# CRC-32のテスト
def test_crc32():
    assert crc32(b'hello') == binascii.crc32(b'hello')
    assert crc32(b'world') == binascii.crc32(b'world')
    assert crc32(b'abcd') == binascii.crc32(b'abcd')

