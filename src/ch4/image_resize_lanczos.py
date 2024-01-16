from PIL import Image
import math
# 画像をリサイズする関数 --- (*1)
def resize(img, size):
    sw, sh = img.size
    dw, dh = size
    scale_x = dw / sw
    scale_y = dh / sh
    nc = 3
    print('size=', sw, sh, '=>', dw, dh, 'scale=', scale_x, scale_y)
    # 空の画像を生成 --- (*3)
    res_img = Image.new('RGB', size)
    brange = lambda x, max_x: max(0, min(int(x), max_x))
    range_move = (-2, -1, 0, 1, 2, 3)
    print(list(range_move))
    # 全ての画素についてフィルタを適用する --- (*4)
    for dy in range(dh):
        for dx in range(dw):
            sy = dy / scale_y
            sx = dx / scale_x
            rr, gg, bb = (0, 0, 0)
            weight_total = 0
            for y in range_move:
                for x in range_move:
                    weight_y = get_weight(y / nc, nc)
                    weight = weight_y * get_weight(x / nc, nc)
                    if weight == 0: continue
                    weight_total += weight
                    # if 1.0 > weight >= 0.01:
                    # print(f'w={abs(weight):.5f}')
                    r, g, b = img.getpixel((
                        brange(sx+x, sw-1), 
                        brange(sy+y, sh-1)))
                    rr += r * weight
                    gg += g * weight
                    bb += b * weight
            rr /= weight_total
            gg /= weight_total
            bb /= weight_total
            color = (brange(rr, 255), brange(gg, 255), brange(bb, 255))
            # print(color)
            res_img.putpixel((dx, dy), color)
    return res_img

def get_weight(d, n):
    d = abs(d)
    if d == 0: return 1.0
    if d > n: return 0
    return sinc(d) * sinc(d / n)
    
def sinc(t):
    return math.sin(t * math.pi) / (t * math.pi)

if __name__ == '__main__':
    for i in [-2,-1, 0, 1, 2, 3]:
        print(i, get_weight(i/3, 3))

    img = Image.open('aaa.png') # 画像を読む
    img = img.convert('RGB') # RGBに変換
    #img = img.crop((400, 150, 700, 450))
    r_img = resize(img, (600, 600)) #
    r_img.save('image_resize_lanczos.png') # 画像を保存


