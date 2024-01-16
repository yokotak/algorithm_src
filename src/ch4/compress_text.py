# ---------------------------------------------------------
# LZ77で圧縮と解凍を行うプログラム
# ---------------------------------------------------------
# プログラムを実行する際
# 以下のコマンドを実行してbitarrayをインストールしてください。
# $ pip3 install bitarray
# ---------------------------------------------------------
# なお、以下のMITライセンスのライブラリを参考に作成しています
# [URL] https://github.com/manassra/LZ77-Compressor
# ---------------------------------------------------------
import math
from bitarray import bitarray

# LZ77で圧縮を行う関数
def lz77_encode(infile, outfile):
    i = 0
    out_buf = bitarray(endian='big')  # 出力用のバッファ
    # ファイルをバイナリファイルとして読み込む
    with open(infile, 'rb') as fp:
        data = fp.read()
    while i < len(data):
        # dataからiの部分一致を探す
        m = findLongestMatch(data, i)
        if m:
            (match_distance, match_len) = m
            out_buf.append(True)
            out_buf.frombytes(bytes([match_distance >> 4]))
            out_buf.frombytes(
                bytes([((match_distance & 0xf) << 4) | match_len]))
            i += match_len
        else:
            # マッチしなければ0ビットのフラグを追加しその後に8ビットを追加
            out_buf.append(False)
            out_buf.frombytes(bytes([data[i]]))
            i += 1
    out_buf.fill()
    # 圧縮したデータをファイルへ書き出す
    with open(outfile, 'wb') as output_file:
        output_file.write(out_buf.tobytes())

# LZ77で解凍を行う関数
def lz77_decode(infile, outfile):
    data = bitarray(endian='big')
    out_buf = []
    # ファイルを読み込む
    with open(infile, 'rb') as input_file:
        data.fromfile(input_file)
    # データを元に戻す
    while len(data) >= 9:
        flag = data.pop(0)
        if not flag:
            byte = data[0:8].tobytes()
            out_buf.append(byte)
            del data[0:8]
        else:
            byte1 = ord(data[0:8].tobytes())
            byte2 = ord(data[8:16].tobytes())
            del data[0:16]
            distance = (byte1 << 4) | (byte2 >> 4)
            length = (byte2 & 0xf)
            for i in range(length):
                out_buf.append(out_buf[-distance])
    out_data = b''.join(out_buf)
    # ファイルへ保存
    with open(outfile, 'wb') as output_file:
        output_file.write(out_data)

# cur_posから始まる部分データの最長一致を検索
def findLongestMatch(data, cur_pos):
    # パラメータを指定
    window_size = 400
    buf_size = 15
    end_of_buffer = min(cur_pos + buf_size, len(data) + 1)
    match_distance = -1
    match_length = -1
    # 部分一致を探す
    for j in range(cur_pos + 2, end_of_buffer):
        start_index = max(0, cur_pos - window_size)
        substring = data[cur_pos:j]
        for i in range(start_index, cur_pos):
            repetitions = len(substring) // (cur_pos - i)
            last = len(substring) % (cur_pos - i)
            matched_string = data[i:cur_pos] * repetitions + data[i:i+last]
            if matched_string == substring and len(substring) > match_length:
                match_distance = cur_pos - i
                match_length = len(substring)
    if match_distance > 0 and match_length > 0:
        return (match_distance, match_length)

if __name__ == "__main__":
    # ファイルを圧縮
    lz77_encode('ginga.txt', 'ginga.lz77')
    print('圧縮しました: ginga.lz77')
    # ファイルを解凍
    lz77_decode('ginga.lz77', 'ginga2.txt')
    print('解凍しました: ginga2.txt')
