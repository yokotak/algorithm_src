# 実行結果を保持する数値リストを作成 --- (*1)
result = [str(i) for i in range(100+1)]
# 3の倍数の要素にFizzを代入 --- (*2)
for i in range(1, 100//3+1):
    result[i*3] = 'Fizz'
# 5の倍数の要素にBuzzを追記 --- (*3)
for i in range(1, 100//5+1):
    result[i*5] = 'Buzz'
# 15の倍数の要素にFizzBuzzを追記 --- (*4)
for i in range(1, 100//15+1):
    result[i*3*5] = 'FizzBuzz'
# 結果を出力 --- (*5)
print('\n'.join(result[1:101]))

