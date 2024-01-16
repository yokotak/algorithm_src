# Base64変換テーブル --- (*1)
TBL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

# バイナリデータをBase64に変換する関数 --- (*2)
def base64_encode(bin_data):
    bin = to_binstr(bin_data) # バイナリデータを2進数文字列に変換 --- (*3)
    if len(bin) % 6 >= 1:
        bin += '0' * (6 - len(bin) % 6) # 6ビットに足りない場合0で補完 --- (*4)
    result = ''
    # 6ビットずつに分けて処理 --- (*5)
    for i in range(len(bin) // 6):
        bit6 = bin[i*6:i*6+6]
        result += TBL[bin_to_dec(bit6)] # 変換テーブルから1文字得る --- (*6)
    if len(result) % 4 >= 1:
        result += '=' * (4 - len(result) % 4) # 4の倍数文字数に揃える --- (*7)
    return result

# データを2進数に変換する --- (*8)
def to_binstr(data):
    result = ''
    for b in data: # 1バイトずつ処理
        bin = ''
        for i in range(8): # 8bitずつ処理
            bin = ('1' if (b >> i) & 1 else '0') + bin
        result += bin
    return result

# 2進数を10進数に変換 --- (*9)
def bin_to_dec(bin_str):
    result = 0
    for c in bin_str:
        result <<= 1
        result += 1 if c == '1' else 0
    return result

# テスト --- (*10)
def test_base64_encode():
    assert to_binstr(b'A') == '01000001'
    assert bin_to_dec('1111') == 15
    assert base64_encode(b'0') == 'MA=='
    assert base64_encode(b'ABCDEFG') == 'QUJDREVGRw=='
    assert base64_encode(b'Hello') == 'SGVsbG8='

if __name__ == '__main__':
    print(base64_encode(b'ABCDEFG'))
