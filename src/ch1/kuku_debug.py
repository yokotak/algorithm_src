# 外側nのfor文
for n in range(1, 9+1):
    print('n=', n) # 変数nを表示
    # 内側mのfor文
    for m in range(1, 9+1):
        value = n * m
        # 九九の結果を表示
        print('    ', n, '*', m, '=', value)
