from PIL import Image
# 白と黒のカラーコードを設定 --- (*1)
WHITE = 255
BLACK = 0

# 画像を二値化する関数 --- (*2)
def binarization(img, threshold):
    # 空の画像をグレイスケールで生成 --- (*3)
    w, h = img.size
    bin_img = Image.new('L', (w, h))
    # 各画素に対して繰り返し二値化を行う --- (*4)
    for y in range(h):
        for x in range(w):
            # 座標からRGBの値を得る --- (*5)
            r, g, b = img.getpixel((x, y))
            # 輝度を計算して二値化 --- (*6)
            p = r * 299/1000 + g * 587/1000 + b * 114/1000
            color = WHITE if p > threshold else BLACK
            # 空の画像に色を書き込む ---(*7)
            bin_img.putpixel((x, y), color)
    return bin_img

if __name__ == '__main__':
    # 画像の読み込んでRGBモードに揃える --- (*8)
    img = Image.open('fuji.jpg')
    img = img.convert(mode='RGB')
    # 二値化して保存 --- (*9)
    img = binarization(img, 120)
    img.save('fuji_bin.png')
