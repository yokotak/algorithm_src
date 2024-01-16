# 線形合同法で乱数を生成する
# 現在時刻(ミリ秒)から乱数シードを得る --- (*1)
from datetime import datetime
rand_seed = int(datetime.now().strftime('%f'))

# 乱数を生成する定数 --- (*2)
A = 1103515245
B = 12345
M = 2 ** 31 - 1 # 31ビットの範囲の整数を利用

# 疑似乱数を生成
def rand():
    global rand_seed # 前回の乱数シードを利用 --- (*3)
    # 疑似乱数を計算する式--- (*4)
    rand_seed = (A * rand_seed + B) % M
    return rand_seed

if __name__ == '__main__':
    for _ in range(5): # 5つ乱数を生成 --- (*5)
        print(rand())
