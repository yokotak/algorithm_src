# ヒープソートを実装したもの --- (*1)
def heapsort(a):
    # 二分ヒープ木の構築 --- (*2)
    for i in range(1, len(a)):
        upheap(a, i)
        print('upheap:', a[:i+1])
    # 二分ヒープ木の親と整列済み領域iを繰り返し交換 --- (*3)
    for i in range(len(a)-1, 0, -1):
        a[i], a[0] = a[0], a[i]  # 木のルートとiを交換 --- (*4)
        # 末尾iを除いて二分ヒープ木を再構築 --- (*5)
        downheap(a, i)
        print('downheap:', a[:i], '→ 整列済', a[i:])
    return a

# i番目の要素をヒープの正しい位置に移動 --- (*6)
def upheap(a, i):
    # 正しい位置に配置されるまで繰り返す
    while i > 0:
        parent = (i - 1) // 2  # 親のインデックス --- (*7)
        if a[parent] >= a[i]:  # 親が子より大きいとき --- (*8)
            break              # 交換しない
        # 親と子を交換
        a[parent], a[i] = a[i], a[parent]
        i = parent

# ルート(0)の要素をヒープ(0からi番目まで)の正しい位置へ移動 --- (*9)
def downheap(a, i):
    if i == 0: return
    parent = 0
    # 正しい位置に配置されるまで繰り返す
    while parent * 2 + 1 < i:
        left = parent * 2 + 1 # 子要素(左)インデックス --- (*10)
        right = parent * 2 + 2 # 子要素(右)インデックス
        child = left # 左右の子要素の大きな方を調べる --- (*11)
        if right < i and a[right] > a[left]:
            child = right
        if a[parent] >= a[child]: # 親が子より大きいとき --- (*12)
            break                 # 交換しない
        # 親と子を交換
        a[parent], a[child] = a[child], a[parent]
        parent = child

# テスト --- (*13)
def test_heapsort():
    assert heapsort([4, 1, 5, 3, 2]) == [1, 2, 3, 4, 5]
    assert heapsort([1, 0, 2]) == [0, 1, 2]
    assert heapsort([2]) == [2]
    assert heapsort([7, 2, 4, 1, 3, 5, 6]) == [1, 2, 3, 4, 5, 6, 7]

if __name__ == '__main__':  # --- (*14)
    print('結果:', heapsort([4, 1, 5, 9, 3, 2, 6, 8, 7]))
