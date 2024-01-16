# PCG(Permuted Congruential Generator)で疑似乱数を生成
from datetime import datetime
multiplier = 6364136223846793005
mask32 = 0xFFFFFFFF
mask64 = 0xFFFFFFFFFFFFFFFF

# 現在時刻で乱数シードを初期化 --- (*1)
# ただし必ず奇数にする
t = int(datetime.now().strftime('%f'))
rand_seed = ((1442695040888963407 + t) * multiplier + 1) & mask64

# PCGで乱数を生成 --- (*2)
def rand_pcg():
    global rand_seed
    x = rand_seed
    count = (x >> 61) & 0b111 # 3ビット取り出す
    rand_seed = (x * multiplier) & mask64
    return bit_rotate_r(x ^ (x >> 22), count) & mask32

# xをkビット右回転する関数 --- (*3)
def bit_rotate_r(x, k):
    return (x >> k) | (x << (32 - k)) & mask32

# 乱数が偏ってないか調べる --- (*4)
def test_rand_pcg():
    for _ in range(100):
        balance = [0, 0, 0, 0, 0, 0]
        for _ in range(600):
            balance[rand_pcg() % 6] += 1
        for i in range(6):
            assert 60 <= balance[i] & balance[i] <= 140

if __name__ == '__main__':
    for _ in range(5): # 5個の乱数を表示 --- (*5)
        print([rand_pcg() % 6 + 1 for _ in range(10)])
