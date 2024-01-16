# シーザー暗号をテストするプログラム(テストのみ作ったもの)
def test_encrypt_caesar():
    assert encrypt('CAT', 3) == 'FDW'
    assert encrypt('LOVE', 3) == 'ORYH'
    assert decrypt('FDW', 3) == 'CAT'

# 暗号化
def encrypt(src, key_no):
    # 後で実装する
    return ''

# 復号化
def decrypt(src, key_no):
    return encrypt(src, key_no * -1)

