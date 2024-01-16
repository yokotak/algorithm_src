import random
# 上下左右を表すリストを用意
udlr = [[0,-1],[0,1],[-1,0],[1,0]]
# 方向をシャッフルして相対座標を得る
random.shuffle(udlr)
dx, dy = udlr[0]
print(dx, dy)
