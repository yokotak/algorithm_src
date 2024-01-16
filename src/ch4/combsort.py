# コムソートを実装した関数 --- (*1)
def combsort(a):
    h = len(a)
    is_swapped = False
    # hが1超で入れ替えがあるまで繰り返す --- (*2)
    while h > 1 or is_swapped:
        is_swapped = False
        h = h * 10 // 13 # 間隔を1.3で割る --- (*3)
        h = 1 if h < 1 else h
        # iを先頭に(i+h)が末尾になるまで繰り返す --- (*4)
        i = 0
        while i+h < len(a):
            if a[i] > a[i+h]: # 入れ替える --- (*5)
                a[i], a[i+h] = a[i+h], a[i]
                is_swapped = True
                print(f'h={h} swap {i},{i+h}', a)
            i += 1
    return a

# PyTest用のテスト --- (*6)
def test_combsort():
    assert combsort([3,1,2]) == [1,2,3]
    assert combsort([5,3,4,2,1]) == [1,2,3,4,5]
    assert combsort([1,5,3]) == [1,3,5]

if __name__ == '__main__':
    # 実行テスト --- (*7)
    print(combsort([5,2,1,4,3]))
