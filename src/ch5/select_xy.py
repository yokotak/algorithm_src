import random
# 壁を作る方向を乱数で決定
r = random.randint(0, 3)
# 乱数の値に応じてif文を順に上下左右の相対座標を得る
if r == 0:
  dx, dy = [0, -1] # 上
elif r == 1:
  dx, dy = [0, 1] # 下
elif r == 2:
  dx, dy = [-1, 0] # 左
elif r == 3:
  dx, dy = [1, 0] # 右
print(dx, dy)
