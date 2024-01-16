from PIL import Image
# ガウシアンフィルタを定義した関数 --- (*1)
def gaussian_filter(img):
    # カーネルを定義 --- (*2)
    k = [
        [ 1/256,  4/256,  6/245,  4/256,  1/256],
        [ 4/256, 16/256, 24/245, 16/256,  4/256],
        [ 6/256, 24/256, 36/245, 24/256,  6/256],
        [ 4/256, 16/256, 24/245, 16/256,  4/256],
        [ 1/256,  4/256,  6/245,  4/256,  1/256]
    ]
    # 空の画像を生成 --- (*3)
    w, h = img.size
    res_img = Image.new('L', (w, h))
    # 全ての画素についてフィルタを適用する --- (*4)
    for y in range(h):
        for x in range(w):
            # カーネルの値を適用 --- (*5)
            total = 0
            for i in range(5):
                for j in range(5):
                    yy = max(0, min(y + i - 2, h-1))
                    xx = max(0, min(x + j - 2, w-1))
                    v = img.getpixel((xx, yy))
                    total += v * k[i][j]
            res_img.putpixel((x, y), int(total))
    return res_img

if __name__ == '__main__':
    # 画像を読む --- (*6)
    img = Image.open('fuji2.jpg')
    # 効果が分かりやすい部分を切り取る --- (*7)
    x, y, w, h = 380, 200, 400, 400
    img = img.crop((x, y, x+w, y+h))
    # グレイスケールに変換
    gray_img = img.convert('L')
    gray_img.save('fuji2_gray.png')
    # ガウシアンフィルタを適用 --- (*8)
    gf_img = gaussian_filter(gray_img)
    # 画像を保存
    gf_img.save('fuji2_gf5x5.png')

