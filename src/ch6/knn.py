import math
# k近傍法で分類問題を解く --- (*1)
def predict(train_data, train_y, test_data, k=3):
    # kの値を確認する
    if k > len(train_data): k = train_data // 2
    if k % 2 == 0: k += 1 # 多数決のため奇数にする
    # 学習データとラベルを一つにまとめて辞書型にする --- (*2)
    train_items = []
    for (x, y) in zip(train_data, train_y):
        train_items.append({'x': x, 'y': y})
    # リスト型のtest_dataの要素を1つずつ予測する --- (*3)
    result = []
    for test_it in test_data:
        # ラベル付き学習データをtest_itに近い順に並び替える --- (*4)
        sort_distance(train_items, test_it)
        # k個の要素を取り出し多数決を取る --- (*5)
        points = {}
        for it in train_items[0:k]:
            label = it['y']
            if label not in points: points[label] = 0
            points[label] += 1
        result.append(max(points, key=points.get))
    return result

# itemsをdataに近い順に並び替える --- (*6)
def sort_distance(items, data):
    for it in items:
        # it と x のユークリッド距離を計算 --- (*7)
        diff = 0
        for i, val in enumerate(data):
            diff += (val - it['x'][i]) ** 2
        it['dist'] = math.sqrt(diff)
    items.sort(key=lambda x:x['dist']) # 並び替える

if __name__ == '__main__': # テストデータで試す --- (*8)
    train_data = [(0, 0), (0, 1), (5, 5), (6, 6)]
    train_label = ['左下', '左下', '右上', '右上']
    test_data = [(1, 1)]
    pred_y = predict(train_data, train_label, test_data)
    print(f'{test_data} → {pred_y}')
