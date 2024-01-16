import ls_distance

# 文字列aとbの類似度を0から1の範囲で返す --- (*1)
def calc_distance_std(a, b):
    mlen = max(len(a), len(b))
    return 1.0 - (ls_distance.calc_distance(a, b) / mlen)

# 分かりやすく説明付きで表示
def print_distance_std(a, b):
    dist = ls_distance.calc_distance(a, b)
    std = calc_distance_std(a, b)
    print(f'+「{a}」と「{b}」')
    print(f'- 距離: {dist}, 類似度: {std}')

if __name__ == '__main__':
    print_distance_std('メロンパン', 'アンパン')
    print_distance_std('甘くて美味しいメロンパン', '美味しいアンパン')
    print_distance_std('ハイシャ', 'カイシャ')
    print_distance_std('カンバン', 'マンハッタン')

