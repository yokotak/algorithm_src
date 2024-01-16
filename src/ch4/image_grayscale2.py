from PIL import Image
img = Image.open('fuji.jpg')
# グレイスケールに変換 --- (*1)
gray_img = img.convert(mode='L')
gray_img.save('fuji_gray2.png')
# グレイスケールを二値化 --- (*2)
bin_img = gray_img.point(lambda x: 255 if x > 120 else 0)
bin_img.save('fuji_bin2.png')
