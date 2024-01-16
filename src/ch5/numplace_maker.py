import pprint, random
import numplace_solve
# 問題を作成する関数 --- (*1)
def shuffle_table(data, blank_rate):
    if len(data) == 0:
        # マスを全部0で初期化 --- (*2)
        data = [[0] * 9 for _ in range(9)]
        # 答えを見つける --- (*3)
        _, data = numplace_solve.solve(data, 0)
    # 繰り返し入れ替えたり回転したりする --- (*4)
    for _ in range(300):
        if random.randint(0, 2) == 0:
            # 上3行と下3列の入れ替えが可能 --- (*5)
            for i in range(3):
                data[0+i], data[6+i] = data[6+i], data[0+i]
        for i in range(3):
            if random.randint(0, 2) == 0:
                # 同じ3×3のマスの行ならば入れ替えが可能 --- (*6)
                l1 = i * 3 + random.randint(0, 2)
                l2 = i * 3 + random.randint(0, 2)
                data[l1], data[l2] = data[l2], data[l1]
        if random.randint(0, 2) == 0:
            # 縦横を入れ替え --- (*7)
            data = [list(x) for x in zip(*data)]
    # ランダムに穴を作る --- (*8)
    for row in range(9):
        for col in range(9):
            if random.random() < blank_rate:
                data[row][col] = 0
    return data

if __name__ == '__main__':
    # ランダムに問題を作成 --- (*9)
    blank_rate = 0.5
    data = shuffle_table([], blank_rate)
    print('--- 問題 ---')
    pprint.pprint(data)
    # 念のため解けるか確認 --- (*10)
    print('--- 答え ---')
    result, data = numplace_solve.solve(data, 0)
    if not result:
        print('[エラー] 壊れています。')
    else:
        pprint.pprint(data)

