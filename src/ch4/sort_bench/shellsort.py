import copy
# シェルソートを実行したもの --- (*1)
def shellsort(a_org):
    a = copy.copy(a_org)
    # 大きめの間隔を選ぶ --- (*2)
    gap = len(a) // 2
    # 間隔が0になるまで繰り返し実行 --- (*3)
    while gap > 0:
        # gap間隔分手前の要素と繰り返し比較して交換 --- (*4)
        for i in range(gap, len(a)):
            # 適切な挿入場所を探す --- (*5)
            tmp = a[i]
            j = i
            while j >= gap and a[j-gap] > tmp:
                a[j] = a[j-gap]
                j -= gap
            if i != j: # 交換する --- (*6)
                a[j] = tmp
                # print(f'gap={gap} swap {i},{j}', a)
        # 間隔を半分にする --- (*7)
        gap = gap // 2
    return a

# テスト --- (*8)
def test_shellsort():
    assert shellsort([5,3,1,2,4]) == [1,2,3,4,5]
    assert shellsort([3,0,7,5]) == [0,3,5,7]
    assert shellsort([8,3,1,2,7,5,6,4]) == [1,2,3,4,5,6,7,8]
    assert shellsort([6,4]) == [4,6]

if __name__ == '__main__': # --- (*9)
    print(shellsort([3, 7, 5, 6, 4, 8, 1, 2]))

