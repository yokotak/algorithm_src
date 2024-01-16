# バブルソートにkey関数を受け取れるようにしたもの --- (*1)
def bsort(a, key):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            # key関数を実行して比較したい値を取り出す --- (*2)
            j_prev = key(a[j-1])
            j_curr = key(a[j])
            # 大小を比較 --- (*3)
            if j_prev > j_curr: 
                a[j], a[j-1] = a[j-1], a[j] # 交換 --- (*4)
    return a

# 対象データ --- (*5)
fruits = [
    {'name': 'リンゴ', 'price': 350}, {'name': 'バナナ', 'price': 210},
    {'name': 'イチゴ', 'price': 820}, {'name': 'ミカン', 'price': 420}
    ]
# 比較関数 --- (*6)
bsort(fruits, key=lambda v: v['price'])
# 結果を出力 --- (*7)
for f in fruits:
    print(f['name'], f['price'])

