from PIL import Image
# 画像をリサイズする関数 --- (*1)
def resize(img, size):
    # サイズを計算 --- (*2)
    sw, sh = img.size
    dw, dh = size
    scale_x = dw / sw
    scale_y = dh / sh
    print('size=', sw, sh, '=>', dw, dh, 'scale=', scale_x, scale_y)
    # 空の画像を生成 --- (*3)
    res_img = Image.new('RGB', size)
    # 全ての画素について繰り返し元画像をコピーする --- (*4)
    for dy in range(dh):
        for dx in range(dw):
            # 元画像の座標を得る --- (*5)
            sx, sy = int(dx / scale_x), int(dy / scale_y)
            r, g, b = img.getpixel((sx, sy))
            res_img.putpixel((dx, dy), (r, g, b))
    return res_img

if __name__ == '__main__':
    img = Image.open('soba.jpg') # 画像を読む --- (*6)
    img = img.convert('RGB') # RGBに変換
    x, y, w, h = 130, 50, 740, 740
    img = img.crop((x, y, x+150, y+150)) # 一部分を切り取る --- (*7)
    r_img = resize(img, (w, h)) # 拡大縮小処理
    r_img.save('image_resize.png') # 画像を保存

