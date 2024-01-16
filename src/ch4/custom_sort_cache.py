# バブルソートでkey関数を受け取れるようにしたものを高速化した
def bsort(a, key):
    # key関数を一度呼び出してキャッシュする
    cache = list(map(lambda v: {'index': key(v), 'link': v}, a))
    # バブルソートを行う
    for i in range(len(cache)):
        for j in range(len(cache)-1, i, -1):
            # key関数を実行して比較したい値を取り出す --- (*2)
            j_prev = cache[j-1]['index']
            j_curr = cache[j]['index']
            # 大小を比較 --- (*3)
            if j_prev > j_curr: 
                cache[j], cache[j-1] = cache[j-1], cache[j] # 交換 --- (*4)
    return list(map(lambda v: v['link'], cache))

# 対象データ --- (*5)
fruits = [
    {'name': 'リンゴ', 'price': 350}, {'name': 'バナナ', 'price': 210},
    {'name': 'イチゴ', 'price': 820}, {'name': 'ミカン', 'price': 420}
    ]
# 比較関数 --- (*6)
fruits2 = bsort(fruits, key=lambda v: v['price'])
# 結果を出力 --- (*7)
for f in fruits2:
    print(f['name'], f['price'])

