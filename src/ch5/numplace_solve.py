import copy, pprint
import numplace_data
# 再帰的にパズルを解く --- (*1)
def solve(data, index):
    # 終了判定
    if index >= 81:
        return True, data
    # 空白か調べる --- (*2)
    row, col = index // 9, index % 9
    if data[row][col] != 0:
        return solve(data, index + 1) # 次のマスを調べる
    # 利用可能な値を調べる --- (*3)
    num_list = get_num_list(data, row, col)
    # 順に値を入れて再帰的に利用可能か調べる --- (*4)
    for n in range(1, 10):
        if num_list[n]: continue
        # 仮の値を入れて再帰的に探す --- (*5)
        tmp_data = copy.deepcopy(data)
        tmp_data[row][col] = n
        result, comp_data = solve(tmp_data, index + 1)
        if result:
            return True, comp_data
    return False, []

# 利用可能な数値を調べる --- (*6)
def get_num_list(data, row, col):
    # 0から9の数値リストをFalseで初期化
    num_list = [False for num in range(10)]
    # 3x3のマス内の値チェック
    my, mx = (row // 3 * 3, col // 3 * 3) # 左上座標
    for yy in range(3):
        for xx in range(3):
            num_list[data[my+yy][mx+xx]] = True
    # 行列のマスの値チェック
    for i in range(9):
        num_list[data[i][col]] = True # 横方向
        num_list[data[row][i]] = True # 縦方向
    return num_list

if __name__ == '__main__': # --- (*7)
    result, data = solve(numplace_data.data, 0)
    if not result:
        print('答えが見つかりませんでした')
    else:
        pprint.pprint(data)

