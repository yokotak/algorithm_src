from PIL import Image
# 8x8のカンマ区切りデータを画像としてファイルに保存 --- (*1)
def draw_and_save(line, savefile):
    # データを数値に変換 --- (*2)
    line_a = line.split(',')
    data = list(map(lambda x: int(x), line_a))
    # ピクセルデータは0から63まで --- (*3)
    image_data = data[0:64]
    label_data = data[64]
    # 画像を描画 --- (*4)
    im = Image.new('L', (8, 8))
    for i, v in enumerate(image_data):
        # ピクセルの座標を計算 --- (*5)
        y = i // 8
        x = i % 8
        # (x, y)に描画 --- (*6)
        c = int(v/16 * 255) # 色を計算
        im.putpixel((x, y), c) # 描画
    # ファイルを保存 --- (*7)
    im.save(savefile)
    print('image=', label_data, 'file=', savefile)

if __name__ == '__main__':
    # CSVファイルを読み込む --- (*8)
    with open('optdigits.tes', 'rt', encoding='utf-8') as fp:
        csv = fp.read()
        lines = csv.split('\n')
    # 画像を取り出して描画 --- (*9)
    draw_and_save(lines[0], 'sample0.png')
    draw_and_save(lines[3], 'sample3.png')
    draw_and_save(lines[9], 'sample9.png')
