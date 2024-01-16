import puzzle15
import copy

# 訪問した盤面を覚えておく --- (*1)
visited = {}
# 再帰的に問題を解く --- (*2)
def solve_r(data, operation, level, max_level):
    if level >= max_level: return [] # 最大レベルになったら戻る
    if data == puzzle15.INIT_LIST: # 盤面が揃ったら終わる
        return operation
    # 現在の盤面を覚えておく --- (*3)
    visited[tuple(data)] = True
    # 上下左右に動かして再帰で確認する --- (*4)
    for no in range(4):
        dir = puzzle15.UDLR[no]
        i1, i2 = puzzle15.calc_index(data, dir)
        if i1 == i2: continue
        # 盤面をコピーして移動する --- (*5)
        tmp = copy.copy(data)
        puzzle15.move(tmp, dir)
        if tuple(tmp) in visited: continue
        # 再帰的に答えを探す --- (*6)
        r = solve_r(tmp, operation+[no], level+1, max_level)
        if len(r) > 0: return r
    return []

def solve(data):
    # 再帰の最大レベルを30から少しずつ増やして検索 --- (*7)
    for max_level in range(30, 80, 5):
        print(f'最大再帰{max_level}回で検索')
        visited.clear()
        result = solve_r(data, [], 0, max_level)
        if len(result) > 0: return result
    print('解けませんでした')
    return []

if __name__ == '__main__':
    # 問題をランダムに生成し答えを表示する --- (*8)
    data = puzzle15.init_game(30)
    result = solve(data)
    print('答え=', result)
    print('手数=', len(result))

