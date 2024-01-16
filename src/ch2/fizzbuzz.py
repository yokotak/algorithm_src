# 1から100まで繰り返す --- (*1)
for n in range(1, 100+1):
    # 変数nについて条件を一つずつ確認していく
    if n % 3 == 0 and n % 5 == 0: # 3の倍数かつ5の倍数のとき --- (*2)
        print('FizzBuzz')
    elif n % 3 == 0:              # 3の倍数のとき --- (*3)
        print('Fizz')
    elif n % 5 == 0:              # 5の倍数のとき --- (*4)
        print('Buzz')
    else:                         # その他のとき --- (*5)
        print(n)

