import puzzle15
import copy
# 幅優先探索を使って問題を解く --- (*1)
def solve(data):
    if data == puzzle15.INIT_LIST: return []
    visited = {} # 訪問した盤面を覚えておく --- (*2)
    queue = [[data, []]] # キューを初期化
    # 答えが見つかるまで繰り返す --- (*3)
    while len(queue) > 0:
        # キューから値を下ろす --- (*4)
        data, result = queue.pop(0)
        # 上下左右を順に探すようにする --- (*5)
        for no, dir in enumerate(puzzle15.UDLR):
            # 移動先のインデックスを得る
            i1, i2 = puzzle15.calc_index(data, dir)
            if i1 == i2: continue
            # 盤面データを複製して数字を移動し完成か確認 --- (*6)
            data2 = copy.copy(data)
            data2[i1], data2[i2] = data2[i2], data2[i1]
            if data2 == puzzle15.INIT_LIST:
                return result+[no]
            # 新規盤面でなければ別の方向を確認 --- (*7)
            if tuple(data2) in visited: continue
            visited[tuple(data2)] = True
            # キューに盤面と手順を追加 --- (*8)
            queue.append([data2, result+[no]])
    return []

if __name__ == '__main__':
    # 問題をランダムに生成し答えを表示する --- (*9)
    data = puzzle15.init_game(30)
    result = solve(data)
    print('答え=', result)
    print('手数=', len(result))

