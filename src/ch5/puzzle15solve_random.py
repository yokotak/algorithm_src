import puzzle15
import random

def solve(data):
    index = 0
    result = []
    while True:
        # 完成したか結果を確認 --- (*1)
        if data == puzzle15.INIT_LIST:
            return result
        # ランダムに穴の位置を動かす --- (*2)
        dir_no = random.randint(0, 3)
        dir = puzzle15.UDLR[dir_no]
        i1, i2 = puzzle15.calc_index(data, dir)
        if i1 == i2: continue
        # あるべき位置に数字があるなら動かさない --- (*3)
        if data[i2] == puzzle15.INIT_LIST[i2]:
            if i2 < index: continue
        # 移動 --- (*4)
        data[i1], data[i2] = data[i2], data[i1]
        result += [dir_no]
        # 移動によって数字が揃えば、indexを更新(上二段まで) --- (*5)
        for i in range(index, 8):
            if data[i] != puzzle15.INIT_LIST[i]: break
            index = i # 現在index番目まで数字が揃っている

if __name__ == '__main__': # --- (*6)
    data = puzzle15.init_game(30)
    result = solve(data)
    print('答え=', result)
    print('手数=', len(result))
