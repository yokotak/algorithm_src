# 二分探索を行う関数 --- (*1)
def binary_search(a, value, min_i, max_i):
    if max_i < min_i:
        return None
    # 中央のインデックスを得る --- (*2)
    i = min_i + (max_i - min_i) // 2
    # 前方にあるか後方にあるか判定 --- (*3)
    if a[i] > value:
        # 前方にある場合 - 範囲を狭めて再帰的に検索 --- (*4)
        return binary_search(a, value, min_i, i-1)
    if a[i] < value:
        # 後方にある場合 - 範囲を狭めて再帰的に検索
        return binary_search(a, value, i+1, max_i)
    # 答えを見つけた --- (*5)
    return i

# テスト --- (*6)
def test_binary_search():
    a = [0,1,2,3,4,5,6,7,8]
    assert binary_search(a, 4, 0, len(a)-1) == 4
    assert binary_search(a, 7, 0, len(a)-1) == 7
    assert binary_search(a, 13, 0, len(a)-1) == None

if __name__ == '__main__':
    # データを二分探索で検索する --- (*7)
    a_list = [1, 9, 8, 2, 3, 4, 5, 7, 6]
    value = 8
    # ソートしておく必要がある
    a_list.sort()
    i = binary_search(a_list, value, 0, len(a_list)-1)
    print('検索結果=', i)

