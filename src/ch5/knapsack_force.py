# ナップサックの最大容量を指定 --- (*1)
MAX_WEIGHT = 9
# 物品の一覧を定義 --- (*2)
ITEMS = [
    {'name': 'A', 'weight': 1, 'price': 730},
    {'name': 'B', 'weight': 2, 'price': 1470},
    {'name': 'C', 'weight': 3, 'price': 2200},
    {'name': 'D', 'weight': 4, 'price': 2870},
    {'name': 'E', 'weight': 5, 'price': 3500},
]
# 再帰的にナップサックに詰める物品を調べる --- (*3)
def pack(result, i, weight, price, knapsack):
    # 最後まで調べたら終わる
    if len(ITEMS) <= i:
        result[knapsack] = price
        return
    # 今回入れる物品
    it = ITEMS[i]
    # 商品iを持たない場合 --- (*4)
    pack(result, i+1, weight, price, knapsack)
    # 商品iを持つ場合 --- (*5)
    knapsack2 = knapsack + it['name']
    weight2 = weight + it['weight']
    price2 = price + it['price']
    # 重量オーバーした？
    if weight2 > MAX_WEIGHT:
        result[knapsack] = price
        return
    # 再帰的に次の物品を詰める
    pack(result, i+1, weight2, price2, knapsack2)

if __name__ == '__main__':
    # 全物品の組合せを確認する --- (*6)
    result = {}
    pack(result, 0, 0, 0, '')
    # 価格が高くなる順に並び替えて価値のある組合せを表示 --- (*7)
    result2 = sorted(result.items(), key=lambda x:x[1], reverse=True)
    print('最も価値のある組合せ=', result2[0])

