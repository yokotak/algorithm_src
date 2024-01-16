import puzzle15
import copy

# 盤面におけるコストを計算する --- (*1)
def calc_cost(data):
    cost = 0
    for i in range(15):
        # i番目のマスについて、完成版面の座標と現在の座標を調べる
        no = puzzle15.INIT_LIST[i]
        i2 = data.index(no)
        y1, x1 = i // 4, i % 4 # 完成版面の座標
        y2, x2 = i2 // 4, i2 % 4 # 現在の座標
        # (x1,y1)から(x2,y2)の距離を求める --- (*2)
        distance = abs(y2 - y1) + abs(x2 - x1)
        cost += distance # 各マスの距離を足す
    return cost

# 幅優先探索の改良版「A*」を使って問題を解く --- (*3)
def solve(data):
    if data == puzzle15.INIT_LIST: return []
    visited = {} # 訪問済み盤面を管理
    queue = [(calc_cost(data), data, [])] # キューを初期化
    # 答えが見つかるまで繰り返す --- (*4)
    while len(queue) > 0:
        # キューから値を下ろす --- (*5)
        cost, data, result = queue.pop(0)
        # 上下左右を順に探す --- (*6)
        for no, dir in enumerate(puzzle15.UDLR):
            # 移動先のインデックスを得る
            i1, i2 = puzzle15.calc_index(data, dir)
            if i1 == i2: continue
            # 盤面データを複製して数字を移動し完成か確認 --- (*7)
            data2 = copy.copy(data)
            data2[i1], data2[i2] = data2[i2], data2[i1]
            if data2 == puzzle15.INIT_LIST:
                return result+[no]
            cost2 = calc_cost(data2)
            # 訪問済みで今回の方がコストが大きいならばキューには追加しない --- (*8)
            if tuple(data2) in visited and cost < cost2:
                continue
            visited[tuple(data2)] = True
            # キューに盤面と手順を追加
            queue.append((cost2, data2, result+[no]))
    return []

if __name__ == '__main__':
    # 問題をランダムに生成し答えを表示する --- (*9)
    data = puzzle15.init_game(30)
    result = solve(data)
    print('答え=', result)
    print('手数=', len(result))

