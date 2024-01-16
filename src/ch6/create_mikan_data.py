import random
import matplotlib.pyplot as plt

# 「mikan.csv」を生成する
OUTFILE = 'mikan.csv'

# サイズの目安
SIZE_2S = 4
SIZE_S = 5
SIZE_M = 6
SIZE_L = 7
SIZE_2L = 8

# 糖度
SUGAR_LOW = 9
SUGAR_HIGH = 12

def create_data(size, sugar):
    r = 0.08
    size_min, size_max = size * (1-r), size * (1+r)
    size_range = size_max - size_min
    size_r = size_min + random.random() * size_range
    sugar_min, sugar_max = sugar * (1-r), sugar * (1+r)
    sugar_range = sugar_max - sugar_min
    sugar_r = sugar_min + random.random() * sugar_range
    return (size_r, sugar_r)

# ミカンのサイズごとの糖度の代表値を指定してデータを生成
data_2s = [create_data(SIZE_2S, SUGAR_HIGH) for _ in range(50)]
data_s = [create_data(SIZE_S, 10.92) for _ in range(50)]
data_m = [create_data(SIZE_M, 10.66) for _ in range(50)]
data_l = [create_data(SIZE_L, 9.56) for _ in range(50)]
data_2l = [create_data(SIZE_2L, SUGAR_LOW) for _ in range(50)]
data = data_2s + data_s + data_m + data_l + data_2l
random.shuffle(data)

# to csv
csv = ''
for o in data:
    csv += f'{o[0]}, {o[1]}\r\n'
# save
with open(OUTFILE, 'wt') as fp:
    fp.write(csv)

# グラフに描画してみる
plt.figure()
for p in data:
    plt.scatter(p[0], p[1])
plt.show()
