# Xorshiftで疑似乱数を生成(yield版)
from datetime import datetime

# Xorshiftで乱数を生成 --- (*1)
def rand_gen():
    # 現在時刻でシードを初期化 -- (*2)
    rand_seed = int(datetime.now().strftime('%f'))
    mask = 0xffffffff
    # 乱数を生成し続ける --- (*3)
    while True:
        y = rand_seed
        y = y ^ (y << 13 & mask)
        y = y ^ (y >> 17)
        y = y ^ (y << 15 & mask)
        rand_seed = y
        yield y # --- (*4)

if __name__ == '__main__':
    # 乱数生成器から次々と乱数を取り出す --- (*5)
    g = rand_gen()
    for i in range(5):
        print(next(g))

