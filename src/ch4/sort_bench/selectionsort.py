import copy

# 選択ソート --- (*1)
def selsort(a_org):
    a = copy.copy(a_org)
    # 先頭から末尾まで繰り返す --- (*2)
    for i in range(len(a)-1):
        # 要素iよりも小さな値を探す --- (*3)
        min_i = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_i]: # 見つけた場合 --- (*4)
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
        # print(f'swap {i}, {min_i}', a)
    return a

# テスト --- (*5)
def test_selsort():
    assert selsort([1,4,5,2,3]) == [1,2,3,4,5]
    assert selsort([3,2,1,0]) == [0,1,2,3]
    assert selsort([4,0,2]) == [0,2,4]

if __name__ == '__main__': # --- (*6)
    print(selsort([4, 5, 2, 1, 3]))

