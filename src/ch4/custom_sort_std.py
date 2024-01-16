# ソート対象データ
fruits = [
    {'name': 'リンゴ', 'price': 350}, {'name': 'バナナ', 'price': 210},
    {'name': 'イチゴ', 'price': 820}, {'name': 'ミカン', 'price': 420}
]
# カスタムソートの実行 --- (*1)
fruits = sorted(fruits, key=lambda v: v['price'])
# 結果を出力
for f in fruits:
    print(f['name'], f['price'])

