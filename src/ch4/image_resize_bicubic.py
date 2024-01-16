from PIL import Image
# 画像をリサイズする関数 --- (*1)
def resize(img, size):
    a = -1
    sw, sh = img.size
    dw, dh = size
    rate = dw / sw
    print('size=', sw, sh, '=>', dw, dh, 'rate=', rate)
    # 空の画像を生成 --- (*3)
    res_img = Image.new('RGB', size)
    brange = lambda x, max_x: max(0, min(int(x), max_x))
    range_move = (-1, 0, 1, 2)
    # 全ての画素についてフィルタを適用する --- (*4)
    for dy in range(dh):
        sy = dy / rate
        range_y = list(map(lambda i: i + sy, range_move))
        for dx in range(dw):
            sx = dx / rate
            range_x = list(map(lambda i: i + sx, range_move))
            rr, gg, bb = (0, 0, 0)
            for y in range_y:
                weight_y = get_weight(y, sy, a)
                for x in range_x:
                    weight = weight_y * get_weight(x, sx, a)
                    if weight == 0: continue
                    print(f'w={weight:.2f}')
                    r, g, b = img.getpixel((brange(x, sw-1), brange(y, sh-1)))
                    rr += r * weight
                    gg += g * weight
                    bb += b * weight
            color = (brange(rr, 255), brange(gg, 255), brange(bb, 255))
            # print(color)
            res_img.putpixel((dx, dy), color)
    return res_img

def get_weight(t1, t2, a):
    d = abs(t1 - t2)
    if d <= 1:
        return (a+2.0) * d * d * d - (a+3.0) * d * d + 1
    elif 1 < d <= 2:
        return a*d*d*d - 5.0*a*d*d + 8.0*a*d - 4.0*a
    else:
        return 0

if __name__ == '__main__':
    img = Image.open('aaa.png') # 画像を読む
    img = img.convert('RGB') # RGBに変換
    #img = img.crop((400, 150, 700, 450))
    r_img = resize(img, (600, 600)) #
    r_img.save('image_resize_bicubic.png') # 画像を保存


