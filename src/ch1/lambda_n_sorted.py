# 文字列のリスト
in_data = ['aa:50', 'bb:20', 'cc:80']

# 普通にソートした場合 --- (*1)
print('普通にソート:')
print(sorted(in_data))

# 文字列の4文字目以降を整数に変換してソート --- (*2)
print('4文字目以降を整数にしてソート:')
print(sorted(in_data, key=lambda s: int(s[3:])))

