import random, math, copy
# k-meansでクラスタリングを行う --- (*1)
def kmeans(data, k, max_iter=1000):
    if len(data) < k: k = len(data)
    # ランダムにk個の中心点を決める --- (*2)
    tmp = copy.copy(data)
    random.shuffle(tmp)
    centroids = tmp[0:k]
    # 中心点と各データの距離を計算して最も各データから近い中心点のIDを得る --- (*3)
    distances = calc_distance(data, centroids) # k個の中心点と各データの距離を計算
    data_ids = [argmin(a) for a in distances] # 最も近い中心点のIDを得る
    # 繰り返しクラスタの中心点を更新 --- (*4)
    for _ in range(max_iter):
        centroids = []
        for id in range(k):
            data_k = []
            for data_id, pt in zip(data_ids, data):
                if data_id == id: data_k.append(pt) # IDのデータのみを抽出 --- (*5)
            centroids.append(calc_average_point(data_k)) # 中心点を求める --- (*6)
        # 再度中心点と各データの距離を計算して最も近いIDを得る --- (*7)
        distances = calc_distance(data, centroids) # 中心点との距離を計算
        data_ids = [argmin(a) for a in distances] # 最も近い中心点のIDを得る
    return data_ids

# ユークリッド距離を計算 --- (*8)
def calc_distance(data, centroids):
    result = []
    for d in data:
        dist = []
        for c in centroids:
            v = math.sqrt((c[0]-d[0])**2 + (c[1]-d[1])**2)
            dist.append(v)
        result.append(dist)
    return result
# 各リストの最も小さな値のID(インデックス)を得る --- (*9)
def argmin(args):
    mv = min(args)
    return args.index(mv)
# データの平均地点を求める --- (*10)
def calc_average_point(points):
    if len(points) == 0: return [0, 0]
    x = sum([p[0] for p in points]) / len(points)
    y = sum([p[1] for p in points]) / len(points)
    return [x, y]

if __name__ == '__main__': # テストデータで試す --- (*11)
    data = [(0,0), (0,1), (1,1), (5,5), (5,4)]
    ids = kmeans(data, 2, 1000)
    print(ids)
