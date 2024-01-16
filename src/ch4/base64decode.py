# Base64変換テーブル --- (*1)
TBL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# Base64デコード --- (*2)
def base64_decode(encoded_str):
    res_bytes = bytearray()
    # TBLを逆引きするための辞書を作成 --- (*3)
    tbl_dict = {}
    for i, c in enumerate(TBL):
        tbl_dict[c] = i
    tbl_dict['='] = 0
    # 4文字ずつ処理 --- (*4)
    for i in range(0, len(encoded_str), 4):
        # 4文字(24ビット)を1つの整数に変換 --- (*5)
        s4 = encoded_str[i:i+4]
        v = 0
        for c in s4:
            v <<= 6
            v += tbl_dict[c]
        # 3バイトに分解 --- (*6)
        res_bytes.append((v >> 16) & 0xff)
        if s4[2] != '=':
            res_bytes.append((v >> 8) & 0xff)
        if s4[3] != '=':
           res_bytes.append((v >> 0) & 0xff)
    return res_bytes


# テスト --- (*7)
def test_base64_decode():
    assert base64_decode('SGVsbG8=') == b'Hello'
    assert base64_decode('QUJDREVGRw==') == b'ABCDEFG'
    assert base64_decode('MA==') == b'0'
    assert base64_decode('Zg==') == b'f'
    assert base64_decode('Zm8=') == b'fo'
    assert base64_decode('Zm9v') == b'foo'
    assert base64_decode('Zm9vYg==') == b'foob'
    assert base64_decode('Zm9vYmE=') == b'fooba'

if __name__ == '__main__':
    print(base64_decode('SGVsbG8='))
