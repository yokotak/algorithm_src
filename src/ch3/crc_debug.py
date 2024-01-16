import binascii
# CRC-32を計算するのに必要な定数
CRC32POLY = 0xEDB88320

# CRC-32を計算する関数 --- (*1)
def crc32(bin_data):
    crc = 0xffffffff # 初期値
    debug_b(crc, '初期値')
    for b in bin_data: # 1バイトずつ繰り返す --- (*2)
        crc ^= b # XOR演算 --- (*3)
        debug_b(b, 'これでXOR')
        debug_b(crc, 'XOR済み')
        print('--- 8bit ---')
        for bit in range(8): # 8回(8ビット分)繰り返す --- (*4)
            debug_b(crc, 'check 1bit')
            if (crc & 1) == 1: # 下位ビットが1か？ --- (*5)
                crc >>= 1
                debug_b(crc, 'shift 1bit')
                crc ^= CRC32POLY # XOR
                debug_b(crc, 'XOR POLY')
            else:
                crc >>= 1
                debug_b(crc, 'shift 1bit')
    return crc ^ 0xffffffff # ビットを反転 --- (*6)

def debug_b(v, memo):
    s = f'{v:032b}'
    s = s[0:8] + ' ' + s[8:16] + ' ' + s[16:24] + ' ' + s[24:]
    print(f'{s} {memo}')

result = crc32(b'a')
debug_b(result, 'reverse bit')
print("0x{:x}".format(result))


