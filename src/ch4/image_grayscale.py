from PIL import Image
# 画像の読み込んでRGBモードに揃える --- (*1)
img = Image.open('fuji.jpg')
img = img.convert(mode='RGB')
# 空のイメージを作成する --- (*2)
w, h = img.size
gray_img = Image.new('L', (w, h))
# グレイスケールに変換 --- (*3)
for y in range(h):
    for x in range(w):
        # 輝度を求めて8ビットグレイスケールとする --- (*4)
        r, g, b = img.getpixel((x, y))
        p = r * 299/1000 + g * 587/1000 + b * 114/1000
        gray_img.putpixel((x, y), int(p))
# 画像を保存 --- (*5)
gray_img.save('fuji_gray.png')
