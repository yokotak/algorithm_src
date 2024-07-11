def dec_to_octa(n):
    result = ''
    while n > 0:
        m = n % 8
        n = n // 8
        result = str(m) + result
    return result

def octa_to_dec(str):
    result = 0
    for i in str:
        result *= 8
        v = 0
        v = ord(i) - ord('0')
        result += v
    return result

if __name__ == "__main__":
    print('dec_to_hex(255)  =>', dec_to_octa(255))
    print('hex_to_dec("888") =>', octa_to_dec('888'))