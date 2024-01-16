# 偶数かどうかを判定する関数 (テストのみ記述したもの)
def is_even(num):
    ''' ------------------------ (*1)
    偶数かどうかを判定する関数
    以下に「>>> テスト」と「期待する結果」を1行ずつ書いている
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    '''
    # 実際のプログラムは空のまま --- (*2)
    return True

# doctestを実行 --- (*3)
if __name__ == '__main__': 
    import doctest
    doctest.testmod()
