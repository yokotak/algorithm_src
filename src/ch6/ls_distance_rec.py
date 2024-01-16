import copy
# 再帰を用いてレーベンシュタイン距離を求める関数 --- (*1)
def calc_distance(a, b, result):
    # 比較元の文字列が空の時、比較先の文字数だけ挿入操作を行う --- (*2)
    if a == '': return result + ['挿入'] * len(b)
    if b == '': return result + ['挿入'] * len(a)
    # 1文字目が同じなら2文字目以降を確認する --- (*3)
    if a[0] == b[0]:
        return calc_distance(a[1:], b[1:], result)
    # 比較先の文字の削除、つまり挿入操作 --- (*4)
    result_tmp = copy.copy(result) + ['挿入']
    del_n = calc_distance(a, b[1:], result_tmp)
    # 比較元の文字の削除、つまり削除操作 --- (*5)
    result_tmp = copy.copy(result) + ['削除']
    ins_n = calc_distance(a[1:], b, result_tmp)
    # 文字の置換 --- 置換操作 --- (*6)
    result_tmp = copy.copy(result) + ['置換']
    rep_n = calc_distance(a[1:], b[1:], result_tmp)
    # 上記の操作で最もコストの少ないモノを採用する --- (*7)
    n = sorted([del_n, ins_n, rep_n], key=lambda x: len(x))
    return n[0]

# 分かりやすく説明つきでレーベンシュタイン距離を表示 --- (*8)
def print_distance(a, b):
    dist = calc_distance(a, b, [])
    print(f'「{a}」と「{b}」の距離: {len(dist)}→{dist}')

if __name__ == '__main__':
    print_distance('メロンパン', 'アンパン')
    print_distance('ハイシャ', 'カイシャ')
    print_distance('カンバン', 'マンハッタン')
