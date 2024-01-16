MAX_WEIGHT = 9 # ナップサックの最大容量を指定
ITEMS = [ # 物品の一覧を定義
    {'name': '*', 'weight': 0, 'price': 0},
    {'name': 'A', 'weight': 1, 'price': 730},
    {'name': 'B', 'weight': 2, 'price': 1470},
    {'name': 'C', 'weight': 3, 'price': 2200},
    {'name': 'D', 'weight': 4, 'price': 2870},
    {'name': 'E', 'weight': 5, 'price': 3500}
]
# 表を作成する関数 --- (*1)
def knapsack_table():
    c = [] # 価値合計の最大値を表す二次元リスト
    g = [] # 物品を持っていくことを選択したかを表す二次元リスト
    for _ in range(len(ITEMS)):
        c.append([0 for _ in range(MAX_WEIGHT+1)])
        g.append([False for _ in range(MAX_WEIGHT+1)])
    # 繰り返し価値の合計の最大値を計算する --- (*2)
    for i, it in enumerate(ITEMS):
        for w in range(1, MAX_WEIGHT+1): # 重さごとに計算
            if it['weight'] <= w:
                # 持っていく場合と持っていかない場合の合計価格 --- (*3)
                v1 = it['price'] + c[i-1][w-it['weight']]
                v2 = c[i-1][w]
                if v1 > v2: # 持っていく方が価値が高い場合
                    c[i][w] = v1
                    g[i][w] = True
                else:
                    c[i][w] = v2
            else:
                c[i][w] = c[i-1][w] # 容量オーバーの場合
    return c, g
# 結果を取得する --- (*4)
def get_result(c, g):
    i, w = (len(ITEMS)-1, MAX_WEIGHT)
    knapsack, price = ('', c[i][w])
    while i > 0 or w > 0:
        if g[i][w]:
            knapsack = ITEMS[i]['name'] + knapsack
            w -= ITEMS[i]['weight']
        i -= 1
    return knapsack, price
# 作成した表を分かりやすく表示する関数 --- (*5)
def show_cg(c, g):
    labels = {True: 'o', False: 'x'}
    for i, it in enumerate(ITEMS):
        if i == 0: # ヘッダ行
            print('| ' + ''.join([f'|{w:6d}' for w in range(MAX_WEIGHT+1)]))
        s = ''
        for w in range(MAX_WEIGHT+1):
            s += f'|{c[i][w]:4d}:{labels[g[i][w]]}'
        print('|' + it['name'] + s)
if __name__ == '__main__':
    # 表を作成し内容を表示 --- (*6)
    c, g = knapsack_table()
    knapsack, price = get_result(c, g)
    show_cg(c, g)
    print('最も価値のある組合せ=', knapsack, price)
