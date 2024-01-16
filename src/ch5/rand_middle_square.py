# 平方採中法で乱数を生成する
# 現在時刻(ミリ秒)から乱数シードを得る --- (*1)
from datetime import datetime
rand_seed = int(datetime.now().strftime('%f'))

def rand():
    global rand_seed # 前回の乱数シードを利用 --- (*2)
    seed = rand_seed
    # 乱数のシードを二乗して、数値を12桁に揃える --- (*3)
    s12 = '{:012}'.format(seed ** 2)
    # 12桁の文字列から5桁抽出する --- (*4)
    rand_seed = int(s12[3:9])
    return rand_seed

if __name__ == '__main__':
   for _ in range(5): # 5つ乱数を生成 --- (*5)
      print(rand())
 