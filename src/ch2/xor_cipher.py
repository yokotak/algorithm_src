import binascii

# 暗号化 --- (*1)
def encrypt(src, key):
    result = bytearray()
    # 文字列をバイト列に変換 --- (*2)
    src_bytes = src.encode()
    key_bytes = key.encode()
    # 1バイトずつXORする --- (*3)
    for i, b in enumerate(src_bytes):
        key_b = key_bytes[i % len(key_bytes)]
        xor_v = b ^ key_b # XOR --- (*4)
        result.append(xor_v)
    # bytearrayをHEX文字列に変換 --- (*5)
    result_s = binascii.b2a_hex(result).decode('utf-8')
    return result_s

# 復号化 --- (*6)
def decrypt(src, key):
    result = bytearray()
    # HEX文字列をバイト列に変換 --- (*7)
    src_b = binascii.a2b_hex(src)
    key_bytes = key.encode()
    # 1バイトずつXORする --- (*8)
    for i, b in enumerate(src_b):
        key_b = key_bytes[i % len(key_bytes)]
        xor_v = b ^ key_b # XOR --- (*9)
        result.append(xor_v)
    # bytearrayを文字列に戻す --- (*10)
    result_s = result.decode('utf-8')
    return result_s

# テスト --- (*11)
def test_encrpyt_xor_cipher():
    assert encrypt('world', 'abc') == '160d110d06'
    assert decrypt('160d110d06', 'abc') == 'world'

if __name__ == '__main__':
    # 'hello'を'abc'で暗号化する --- (*12)
    enc = encrypt('hello', 'abc')
    dec = decrypt(enc, 'abc')
    print('暗号化:', enc)
    print('復号化:', dec)
