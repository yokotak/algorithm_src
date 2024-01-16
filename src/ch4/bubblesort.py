# バブルソート --- (*1)
def bubblesort(a):
    # 繰り返し交換する --- (*2)
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j-1] > a[j]: # 隣の要素と比較 --- (*3)
                a[j], a[j-1] = a[j-1], a[j] # 交換 --- (*4)
                print(f'swap {j-1},{j}', a)
    return a

# テスト --- (*5)
def test_bubblesort():
    assert bubblesort([5,1,4,3,2]) == [1,2,3,4,5]
    assert bubblesort([3,3,1]) == [1,3,3]
    assert bubblesort([2,1,0]) == [0,1,2]

if __name__ == '__main__':
    # 実行テスト --- (*6)
    print(bubblesort([5, 2, 4, 1, 3]))

