# レーベンシュタイン距離を求める関数 --- (*1)
def calc_distance(a, b):
    # aとbが同じなら距離は0 --- (*2)
    if a == b: return 0
    # aやbが空の場合を考慮
    if a == '': return len(b)
    if b == '': return len(a)
    # 二次元の表を用意する --- (*3)
    matrix = [ [0]*(len(b)+1) for _ in range(len(a)+1) ]
    # 0の時の初期値をセット
    for i in range(len(a)+1):
        matrix[i][0] = i
    for j in range(len(b)+1):
        matrix[0][j] = j
    # 表を埋めていく --- (*4)
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            replace_cost = 0 if a[i-1] == b[j-1] else 1
            # 最小距離を採用する --- (*5)
            matrix[i][j] = min([
                matrix[i-1][j] + 1, # 文字の挿入
                matrix[i][j-1] + 1, # 文字の削除
                matrix[i-1][j-1] + replace_cost, # 文字の置換
            ])
    # 右下の値が答え --- (*6)
    return matrix[len(a)][len(b)]

# 分かりやすく説明つきでレーベンシュタイン距離を表示 --- (*7)
def print_distance(a, b):
    dist = calc_distance(a, b)
    print(f'「{a}」と「{b}」の距離: {dist}')

if __name__ == '__main__':
    print_distance('メロンパン', 'アンパン')
    print_distance('ハイシャ', 'カイシャ')
    print_distance('カンバン', 'マンハッタン')
