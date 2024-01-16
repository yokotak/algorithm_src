import matplotlib.pyplot as plt
import random
import kmeans

# データをランダムに生成する --- (*1)
def create_data(cx, cy, r):
    x = cx + random.randint(0, r) - r // 2
    y = cy + random.randint(0, r) - r // 2
    return (x, y)

# データをたくさん生成 --- (*2)
data1 = [create_data(20, 20, 30) for _ in range(100)]
data2 = [create_data(50, 50, 30) for _ in range(100)]
data3 = [create_data(80, 20, 30) for _ in range(100)]
data = data1 + data2 + data3
# クラスタリング --- (*3)
ids = kmeans.kmeans(data, 3)
# グラフにプロット --- (*4)
colors = ['red', 'blue', 'green']
markers = ['o', 's', '^']
plt.figure()
for p, id in zip(data, ids):
    plt.scatter(p[0], p[1], color=colors[id], marker=markers[id])
plt.show()
