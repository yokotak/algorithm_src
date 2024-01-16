import matplotlib.pyplot as plt
import kmeans

# ミカンデータ「mikan.csv」を読み込む --- (*1)
with open('mikan.csv', 'rt') as fp:
    csv = fp.read()
# ミカンデータCSVを二次元のリストに変換 --- (*2)
data = []
for line in csv.split('\n'):
    line_a = line.split(',')
    if len(line_a) < 2: continue
    size_s, sugar_s = line_a
    size, sugar = float(size_s.strip()), float(sugar_s.strip())
    data.append((size, sugar))

# k-means法でクラスタリング --- (*3)
data_ids = kmeans.kmeans(data, 3, 1000)

# グラフに描画 --- (*4)
colors = ['red', 'blue', 'green']
markers = ['o', 's', '^']
plt.figure()
for p, id in zip(data, data_ids):
    plt.scatter(p[0], p[1], color=colors[id], marker=markers[id])
plt.show()
