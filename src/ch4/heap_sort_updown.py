# ヒープソートを実装したもの --- (*1)
def heapsort(a):
    # ヒープを構成する --- (*2)
    for i in range(len(a)):
        upheap(a, i)
        print(f'upheap:i={i}', a)
    # ヒープの再構成 --- (*3)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        downheap(a, i-1)
        print(f'downheap:i={i}', a)
    return a

# ヒープを構成する関数 --- (*4)
def upheap(a, n):
    # 繰り返し親子を交換 --- (*5)
    while n > 0:
        # 親を決定
        parent = (n - 1) // 2
        # 親に大きな値が渡るよう交換 --- (*6)
        if a[parent] < a[n]:
            a[n], a[parent] = a[parent], a[n]
            print(f'parent={parent} swap={n},{parent}')
            n = parent
        else:
            break

# 
def downheap(a, n):
    if n == 0:
        return
    parent = 0
    while True:
        child = 2 * parent + 1
        if child > n:
            break
        if child < n and a[child] < a[child + 1]:
            child += 1
        if a[parent] < a[child]:
            a[child], a[parent] = a[parent], a[child]
            parent = child
        else:
            break

def test_heapsort():
    assert heapsort([4,1,5,3,2]) == [1,2,3,4,5]
    assert heapsort([1,0,2]) == [0,1,2]
    assert heapsort([2]) == [2]
    assert heapsort([7,2,4,1,3,5,6]) == [1,2,3,4,5,6,7]

if __name__ == '__main__':
    print(heapsort([4,1,5,3,2]))
