from PIL import Image, ImageDraw

# 迷路データを画像ファイルに保存する関数 --- (*1)
def draw(maze, filename, w=18):
    # 空の画像を作成 --- (*2)
    rows,cols = len(maze), len(maze[0]) # 画像サイズを計算
    im = Image.new('RGB', (w*cols, w*rows))
    # 迷路をImageに描画する --- (*3)
    imd = ImageDraw.Draw(im)
    colors = ['white', 'brown', 'aqua']
    for y, lines in enumerate(maze):
        for x, no in enumerate(lines):
            yy, xx = y*w, x*w
            imd.rectangle([(xx, yy), (xx+w, yy+w)], fill=colors[no])
    # 画像を保存 --- (*4)
    im.save(filename)

if __name__ == '__main__': # 描画テスト--- (*5)
   draw([[1,1,1,1,1,1,1],
        [1,0,1,0,0,0,1],
        [1,0,0,0,1,0,1],
        [1,0,1,0,1,0,1],
        [1,1,1,1,1,1,1]], 'maze_test.png')
