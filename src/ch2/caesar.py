# シーザー暗号のプログラム(完成版)

# シーザー暗号をテストする関数
def test_encrypt_caesar():
    assert encrypt('CAT', 3) == 'FDW'
    assert encrypt('LOVE', 3) == 'ORYH'
    assert decrypt('FDW', 3) == 'CAT'

# 暗号化
def encrypt(src, key_no):
    result = ''
    # 1文字ずつ処理する --- (*1)
    for c in src:
        # 大文字ならkey_no分ずらす --- (*2)
        if 'A' <= c <= 'Z':
            ci = ord(c)  # 文字を文字コードに変換 --- (*3)
            base = ord('A')  # 'A'の文字コードを取得
            ci = (ci - base + key_no) % 26 + base  # --- (*4)
            c = chr(ci) # 文字コードを文字に変換 --- (*5)
        # 変換結果を追加 --- (*6)
        result += c
    return result

# 復号化
def decrypt(src, key_no):
    return encrypt(src, key_no * -1)
