from huffman_encode import huffman_encode

# ハフマン圧縮で復号する関数 --- (*1)
def huffman_decode(code_dict, bindata):
    # ハフマン木の辞書のキーと値を逆にする --- (*2)
    code2_dict = {v: k for k,v in code_dict.items()}
    # 繰り返し2進数データを辞書のキーと照合して復号する --- (*3)
    result = ''
    key = ''
    for bit in bindata:
        key += bit
        # キーが辞書に存在するかを確認 --- (*4)
        if key in code2_dict:
            result += code2_dict[key]
            key = ''
    return result

if __name__ == '__main__':
    # ハフマン圧縮 ---- (*5)
    bindata, code_dict = huffman_encode('CDE^CDE^GEDCDED^')
    print('encode=', bindata)
    # 圧縮されたデータを復号する --- (*6)
    decoded = huffman_decode(code_dict, bindata)
    print('decode=', decoded)
