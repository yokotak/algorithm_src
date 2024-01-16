# クイックソートを実装したもの --- (*1)
def quicksort(a):
    if len(a) == 0:
        return []
    # 基準値(ピボット)を決める --- (*2)
    pivot = a[len(a) // 2]
    # 基準値よりも小さい,大きい,同じリストを用意 --- (*3)
    left, right, middle = [], [], []
    # 繰り返しaの各値を確認 --- (*4)
    for v in a:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            middle.append(v)
    # print(f'pivot={pivot}', left, '<', middle, '<', right)
    # 基準値よりも小さい値を再帰的にソート --- (*5)
    left = quicksort(left)
    # 基準値よりも大きい値を再帰的にソート
    right = quicksort(right)
    # 小さい + 同じ + 大きいリストを結合して返す --- (*6)
    return left + middle + right

# テスト --- (*7)
def test_quicksort():
    assert quicksort([]) == []
    assert quicksort([3,2,1,4]) == [1,2,3,4]
    assert quicksort([3,1,1,2]) == [1,1,2,3]
    assert quicksort([2,0,6,4]) == [0,2,4,6]

if __name__ == '__main__': # --- (*8)
    print(quicksort([2, 5, 1, 3, 4, 6]))

