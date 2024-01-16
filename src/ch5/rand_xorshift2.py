# Xorshiftで疑似乱数を生成

# 乱数シードの初期化(4つの整数を指定) --- (*1)
x, y, z, w = (123456789,362436069,521288629,84871234)

# 現在時刻で乱数シードを初期化 --- (*2)
from datetime import datetime
x = int(datetime.now().strftime('%f'))

# Xorshiftで乱数を生成 --- (*3)
def rand():
    global x,y,z,w
    t = x ^ (x << 11) & 0xffffffff
    x, y, z = y, z, w
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8)) & 0xffffffff
    return w

if __name__ == '__main__':
    for _ in range(5): # 5個の乱数を表示 --- (*4)
        print(rand())
