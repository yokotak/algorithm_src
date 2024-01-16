from PIL import Image
import math, json
# 画像をリサイズする関数 --- (*1)
def resize(img, size):
    sw, sh = img.size
    dw, dh = size
    scale_x = dw / sw
    scale_y = dh / sh
    print('size=', sw, sh, '=>', dw, dh, 'scale=', scale_x, scale_y)
    # 空の画像を生成
    res_img = Image.new('RGB', size)
    # 全ての画素について繰り返し元画像をコピーする --- (*2)
    for dy in range(dh):
        for dx in range(dw):
            # 元画像の座標を得る --- (*3)
            sy, sx = dy / scale_y, dx / scale_x
            # 周囲4点の座標を得る --- (*4)
            sy0, sx0 = int(sy), int(sx)
            sy1, sx1 = min(sy0+1, sh - 1), min(sx0+1, sw - 1)
            # 4点の色を得る
            p00 = img.getpixel((sx0, sy0))
            p01 = img.getpixel((sx0, sy1))
            p10 = img.getpixel((sx1, sy0))
            p11 = img.getpixel((sx1, sy1))
            # 重みを計算 --- (*5)
            wx = sx - sx0
            wy = sy - sy0
            # 重みに沿って色を混ぜる
            rgb = [0,0,0]
            for i in range(3): # RGB
                rgb[i] = int((1-wx) * (1-wy) * p00[i] + \
                        wx * (1-wy) * p10[i] + \
                        (1-wx) * wy * p01[i] + \
                        wx * wy * p11[i])
            res_img.putpixel((dx, dy), tuple(rgb))
    return res_img

if __name__ == '__main__':
    img = Image.open('soba.jpg') # 画像を読む --- (*6)
    img = img.convert('RGB') # RGBに変換
    x, y, w, h = 130, 50, 740, 740
    img = img.crop((x, y, x+150, y+150)) # 一部分を切り取る
    r_img = resize(img, (w, h)) # 拡大縮小処理
    r_img.save('image_resize2.png') # 画像を保存

