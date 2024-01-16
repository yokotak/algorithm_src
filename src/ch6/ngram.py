# n-gramを生成する --- (*1)
def ngram(s, n):
    result = []
    nlen = len(s) - n + 1
    for i in range(nlen):
        result.append(s[i:i+n])
    return result

# 類似度を調べる --- (*2)
def calc_similarity(a, b, n):
    a_list = set(ngram(a, n)) # n-gramをユニークにする
    b_list = set(ngram(b, n)) #
    # 合致する語彙をカウントする --- (*3)
    cnt = 0
    for aw in a_list:
        for bw in b_list:
            if aw == bw:
                cnt += 1
    return cnt / max(len(a_list), len(b_list))

# 類似度を調べて説明を表示する
def print_similarity(a, b):
    v = calc_similarity(a, b, 2)
    print(f'+「{a}」と「{b}」')
    print(f'- 類似度: {v}')

if __name__ == '__main__':
    print_similarity('メロンパン', 'アンパン')
    print_similarity('甘くて美味しいメロンパン', '美味しいアンパン')
    print_similarity('ハイシャ', 'カイシャ')
    print_similarity('猫はネズミを追う', 'ネズミを猫は追う')
