# Xorshiftで疑似乱数を生成

# 現在時刻で乱数シードを初期化 --- (*1)
from datetime import datetime
rand_seed = int(datetime.now().strftime('%f'))

# Xorshiftで乱数を生成 --- (*2)
def rand():
    global rand_seed
    mask = 0xffffffff
    y = rand_seed
    y = y ^ (y << 13 & mask) # --- (*3)
    y = y ^ (y >> 17)
    y = y ^ (y << 15 & mask)
    rand_seed = y
    return y

if __name__ == '__main__':
    for _ in range(5): # 5個の乱数を表示 --- (*4)
        print(rand())
