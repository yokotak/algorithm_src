# マージソートを実装する関数 --- (*1)
def mergesort(a):
    if len(a) <= 1:
        return a
    # リストを分割する --- (*2)
    mi = len(a) // 2 # 中央値を調べる
    left = mergesort(a[:mi]) # 分割して左側を並べる
    right = mergesort(a[mi:]) # 分割して右側を並べる
    # 結合して戻す --- (*3)
    return list(merge_list(left, right))

# 分割したリストを結合する --- (*4)
def merge_list(left, right):
    # print(left, right)
    result = []
    left_i, right_i = 0, 0
    # 左右のリストを並び替えながら結合 --- (*5)
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    # 左右に残りがあれば追加 --- (*6)
    if left_i < len(left) :
        result.extend(left[left_i:])
    if right_i < len(right):
        result.extend(right[right_i:])
    return result

# テスト --- (*7)
def test_mergesort():
    assert mergesort([1,3,2,4,5]) == [1,2,3,4,5]
    assert mergesort([5,3,1,2,4]) == [1,2,3,4,5]
    assert mergesort([3,0,7,5]) == [0,3,5,7]

if __name__ == '__main__': # --- (*8)
    print(mergesort([2,1,4,7,6,3,5]))

