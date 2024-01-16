from PIL import Image
import image_resize
import image_resize2

if __name__ == '__main__':
    img = Image.open('soba.jpg') # 画像を読む --- (*6)
    img = img.convert('RGB') # RGBに変換
    x, y, w, h = 130, 50, 740, 740
    img = img.crop((x, y, x+150, y+150)) # 一部分を切り取る
    r_img1 = image_resize.resize(img, (w, h)) # 拡大縮小処理
    r_img1.save('image_resize.png') # 画像を保存
    r_img2 = image_resize2.resize(img, (w, h)) # 拡大縮小処理
    r_img2.save('image_resize2.png') # 画像を保存

