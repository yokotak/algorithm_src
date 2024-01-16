import copy
# ヒープソートを実装したもの --- (*1)
def heapsort(a_org):
    a = copy.copy(a_org)
    # 二分ヒープ木の構築 --- (*2)
    for i in range(len(a), -1, -1):
        heapify(a, len(a), i)
    # print('構築直後の木:', a)
    # 二分ヒープ木の親と整列済み領域iを繰り返し交換 --- (*3)
    for i in range(len(a)-1, 0, -1):
        a[i], a[0] = a[0], a[i] # 木のルートとiを交換 --- (*4)
        # 末尾iを除いて二分ヒープ木を再構築 --- (*5)
        heapify(a, i, 0)
        # print('木', a[:i], '→ 整列済', a[i:])
    return a

# 最大二分ヒープ木を構築 --- (*6)
def heapify(a, size, parent):
    largest = parent # 親
    left = parent * 2 + 1 # 左側の子要素
    right = parent * 2 + 2 # 右側の子要素
    # 左側の子要素が親より大きいか？ --- (*7)
    if left < size and a[parent] < a[left]:
        largest = left
    # 右側の子要素が親より大きいか？
    if right < size and a[largest] < a[right]:
        largest = right
    # 親子関係が反転していれば値を交換 --- (*8)
    if largest != parent:
        a[parent], a[largest] = a[largest], a[parent] # 交換
        # 再帰的に親子関係を変更 --- (*9)
        heapify(a, size, largest) 

# テスト --- (*10)
def test_heapsort():
    assert heapsort([4,1,5,3,2]) == [1,2,3,4,5]
    assert heapsort([1,0,2]) == [0,1,2]
    assert heapsort([2]) == [2]
    assert heapsort([7,2,4,1,3,5,6]) == [1,2,3,4,5,6,7]

if __name__ == '__main__': # --- (*11)
    print(heapsort([4,1,5,3,2]))
