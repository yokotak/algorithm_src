import sha256_const
# SHA-256のハッシュを求める関数 --- (*1)
def sha256(msg):
    # ハッシュを初期化する --- (*2)
    hi = [sha256_const.SHA256H[i] for i in range(8)]
    # ブロックサイズに合うようにパディング --- (*3)
    msg = bytearray(msg)
    pad = padding(msg, 64)
    # ブロックサイズで区切って繰り返し処理する --- (*4)
    msg_blocks = split_bytes(pad, 64)
    for block in msg_blocks:
        sha256_block(block, hi)
    # HEX文字列で出力
    return ''.join(map(r'{:08x}'.format, hi))

# ビットローテーションを行う --- (*5)
def rotr(x, y):
    return ((x >> y) | (x << (32 - y))) & 0xFFFFFFFF

# 64ビットのブロックを処理 --- (*6)
def sha256_block(block, hi):
    # 64バイトを32ビットずつ16個のリストに分割 --- (*7)
    w = []
    for i in range(16):
        v = (block[i*4+0] << 24) + (block[i*4+1] << 16) + \
            (block[i*4+2] << 8)  + (block[i*4+3])
        w.append(v)
    # 続く16から63バイトまでをローテーション計算
    for i in range(16, 64):
        s0 = rotr(w[i-15], 7) ^ rotr(w[i-15], 18) ^ (w[i-15] >> 3)
        s1 = rotr(w[i-2], 17) ^ rotr(w[i-2], 19) ^ (w[i-2] >> 10)
        w.append((w[i-16] + s0 + w[i -7] + s1) & 0xFFFFFFFF)
    # 変数をハッシュで初期化 --- (*8)
    a,b,c,d,e,f,g,h = [hi[i] for i in range(8)]
    # ローテーション処理 
    for i in range(64):
        s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = s0 + maj
        s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
        ch = (e & f) ^ ((~e) & g)
        temp1 = h + s1 + ch + sha256_const.SHA256K[i] + w[i]
        h, g, f = g, f, e
        e = (d + temp1) & 0xFFFFFFFF
        d, c, b = c, b, a
        a = (temp1 + temp2) & 0xFFFFFFFF
    # ハッシュの値を更新
    h2 = (a,b,c,d,e,f,g,h)
    for i in range(8):
        hi[i] = (hi[i] + h2[i]) & 0xFFFFFFFF

# データを指定サイズに合うように詰め物をする --- (*9)
def padding(msg, size):
    bits, mod = (len(msg) * 8, len(msg) % size)
    padcount = size - mod
    if mod > size - 8:
        padcount += 64
    for i in range(padcount):
        msg.append(0x80 if i == 0 else 0)
    # 最後の8バイトは入力のビット数を指定
    for i in range(1, 8+1):
        msg[len(msg) - i] = bits & 0xFF
        bits >>= 8
    return msg

# データを指定バイトごとに区切る --- (*10)
def split_bytes(msg, size):
    a = []
    n = len(msg) // size + (0 if len(msg) % size == 0 else 1)
    for i in range(n):
        a.append(msg[i*size:(i+1)*size])
    return a

# SHA-256をテストする --- (*11)
import hashlib
def test_sha256():
    assert sha256(b'hello') == hashlib.sha256(b'hello').hexdigest()
    assert sha256(b'world') == hashlib.sha256(b'world').hexdigest()
    assert sha256(b'test') == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'
