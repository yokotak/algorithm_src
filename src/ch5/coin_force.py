# コイン一覧を定義
COIN_LIST = [
    {'name': '$1', 'value': 1},
    {'name': '$2', 'value': 2},
    {'name': '$7', 'value': 7},
    {'name': '$8', 'value': 8},
    {'name': '$12', 'value': 12},
    {'name': '$50', 'value': 50},
]
# 全探索法で再帰的に組合せを調べる関数 --- (*1)
def coin_search(result, amount, i, value, nums, names):
    if i >= len(COIN_LIST) or amount < value:
        return
    if amount == value: # 額ぴったりになれば結果に追加
        result.append([nums, names])
        return
    # このコインを使わない場合 --- (*2)
    coin_search(result, amount, i+1, value, nums, names)
    # このコインを使う場合 --- (*3)
    nums += 1
    value += COIN_LIST[i]['value']
    names += COIN_LIST[i]['name']
    coin_search(result, amount, i+1, value, nums, names)
    # さらにもう一枚同じコインを使う場合 --- (*4)
    coin_search(result, amount, i, value, nums, names)
# 支払額を指定して最小の組合せを求める関数 --- (*5)
def coin_search_result(amount):
    result = []
    coin_search(result, amount, 0, 0, 0, '')
    result = sorted(result, key=lambda v: v[0])
    return result[0]

if __name__ == '__main__':
    # $15と$99の値を調査 --- (*6)
    nums, names = coin_search_result(15)
    print(f'$15の場合: 最小枚数={nums}枚, 組合せ={names}')
    nums, names = coin_search_result(99)
    print(f'$99の場合: 最小枚数={nums}枚, 組合せ={names}')
