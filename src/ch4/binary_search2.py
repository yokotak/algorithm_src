# 二分探索を行う関数 --- (*1)
def binary_search(a, value, fn, min_i, max_i):
    if max_i < min_i:
        return None
    i = min_i + (max_i - min_i) // 2 # 中央のインデックス
    # 前方にあるか後方にあるか判定して範囲を狭めて再帰的に検索
    if fn(a[i]) > fn(value):
        return binary_search(a, value, fn, min_i, i-1)
    if fn(a[i]) < fn(value):
        return binary_search(a, value, fn, i+1, max_i)
    return a[i] # 結果の辞書型を返す

if __name__ == '__main__':
    # 例題を解く --- (*2)
    a_list = [1, 9, 8, 2, 3, 4, 5, 7, 6]
    value = 8
    # ソート前にリストを辞書型に変換しインデックスを記憶 --- (*3)
    a_list2 = [{'i': i, 'v': v} for i, v in enumerate(a_list)]
    v_dict = {'i': -1, 'v': value}
    # インデックス取得用のlambdaを用意
    fn = lambda x:x['v']
    # 辞書型をソートする --- (*4)
    a_list2.sort(key=fn)
    # 二分探索を行う --- (*5)
    result = binary_search(a_list2, v_dict, fn, 0, len(a_list2)-1)
    print('元データ:', a_list)
    print('検索結果:', result)
    print(f'値{value}は(0から数えて){result["i"]}番目にあります')


