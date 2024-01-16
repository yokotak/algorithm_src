# シーザー暗号を大文字と小文字でテスト
def test_encrypt_caesar2():
    assert encrypt('CAT', 3) == 'FDW'
    assert encrypt('love', 3) == 'oryh'
    assert decrypt('fdw', 3) == 'cat'

# 暗号化
def encrypt(src, key_no):
    result = ''
    # 1文字ずつ処理する --- (*1)
    for c in src:
        # 小文字の場合 --- (*2)
        if 'a' <= c <= 'z':
            base = ord('a')
            c = chr((ord(c) - base + key_no) % 26 + base)
        # 大文字の場合 --- (*3)
        elif 'A' <= c <= 'Z':
            base = ord('A')
            c = chr((ord(c) - base + key_no) % 26 + base)
        result += c
    return result

# 復号化
def decrypt(src, key_no):
    return encrypt(src, key_no * -1)
