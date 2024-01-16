# 挿入ソート --- (*1)
def insertion_sort(a):
    # リストを末尾まで繰り返す(iは未処理の先頭を指す) --- (*2)
    for i in range(1, len(a)):
        print(f'i={i}')
        # 整列済みの中から挿入先を検索 --- (*3)
        j = i
        while (j > 0) and (a[j-1] > a[j]):
            a[j-1], a[j] = a[j], a[j-1]  # 交換 --- (*4)
            print(f'swap {j-1}, {j}', a)
            j -= 1
    return a

# テスト --- (*5)
def test_insertion_sort():
    assert insertion_sort([3, 5, 4, 1, 2]) == [1, 2, 3, 4, 5]
    assert insertion_sort([4, 0, 2]) == [0, 2, 4]
    assert insertion_sort([6, 1, 2, 4, 5, 3]) == [1, 2, 3, 4, 5, 6]

if __name__ == '__main__':  # --- (*6)
    print(insertion_sort([3, 5, 4, 1, 2]))
