# コイン一覧を定義 --- (*1)
COIN_LIST = [
    {'name': '*', 'value': 0},
    {'name': '$1', 'value': 1},
    {'name': '$2', 'value': 2},
    {'name': '$7', 'value': 7},
    {'name': '$8', 'value': 8},
    {'name': '$12', 'value': 12},
    {'name': '$50', 'value': 50},
]
# 表を作成する関数 --- (*2)
def coin_search(value):
    c = [] # コイン枚数を表す二次元リスト
    g = [] # コインの組合せを保持する二次元リスト
    for _ in range(len(COIN_LIST)):
        c.append([0 for _ in range(value+1)])
        g.append(['' for _ in range(value+1)])
    # 繰り返し最小枚数を計算する --- (*3)
    for i, it in enumerate(COIN_LIST):
        for v in range(1, value+1):
            if i == 0 or v == 0:
                c[i][v] = 0
                continue
            # 前回の値と比較する --- (*4)
            prev_nums = c[i-1][v]
            curr_nums, names = get_coin_min_nums(i, v)
            # 今回の組合せが最短か
            if prev_nums == 0 or curr_nums < prev_nums:
                c[i][v] = curr_nums
                g[i][v] = names
            else:
                c[i][v] = prev_nums
    # 結果を求める --- (*5)
    i = len(COIN_LIST)-1
    names, nums = '', 0
    while names == '' and i > 0:
        names, nums = g[i][value], c[i][value]
        i -= 1
    return nums, names
# 与えられたコインを使った場合の最小枚数を調べる --- (*6)
def get_coin_min_nums(i, value):
    names = ''
    amount = value
    cnt = 0
    while amount > 0 and i > 0:
        if COIN_LIST[i]['value'] > amount:
            i -= 1
            continue
        amount -= COIN_LIST[i]['value']
        names += COIN_LIST[i]['name']
        cnt += 1
    return cnt, names
if __name__ == '__main__':
    # $15と$99の値を調査
    nums, names = coin_search(15)
    print(f'$15の場合: 最小枚数={nums}枚, 組合せ={names}')
    nums, names = coin_search(99)
    print(f'$99の場合: 最小枚数={nums}枚, 組合せ={names}')

