import tkinter as tk, copy

# 柱と円盤の初期状態を設定 --- (*1)
cols = [[1,2,3,4,5], [], []]

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.geometry('800x350')
cv = tk.Canvas(win, width=800, height=350, bg='white')
cv.pack()
# 柱を描画する --- (*3)
def draw_pillar(no):
    margin = 10 # 余白
    col_width = 800 // 3 # 描画域の幅
    col_x = no * col_width # 左端のX座標
    dh, dw = 50, (col_width - margin * 2) # 円盤の高さと幅
    by = margin + dh * 6 # 地上のY座標
    cx = col_x + col_width // 2 # 柱のX座標
    cv.create_line(cx, margin, cx, by, fill='silver', width=5) # 柱
    cv.create_line(col_x, by, col_x+col_width, by, fill='silver', width=5) # 地
    # 円盤リストの先頭に0を詰める --- (*4)
    disks = copy.copy(cols[no])
    while len(disks) < 5:
        disks.insert(0, 0)
    # 円盤を描画する --- (*5)
    for i, w in enumerate(disks):
        if w == 0: continue # 0 なら何も描画しない
        dx = col_x + (col_width - dw) // 2 # 円盤のX座標
        dy = margin + dh // 2 + i * dh # 円盤のY座標
        sm = (5 - w) * 15 # 円盤のサイズ補正
        cv.create_rectangle(dx + sm, dy, dx+dw - sm, dy + dh - 10,
            fill=('orange' if w % 2 == 0 else 'yellow')) # 円盤を描画
# 全ての柱を描画する --- (*6)
def draw_pillars():
    cv.delete('all') # 画面をクリア
    for no in range(3):
        draw_pillar(no)

# ハノイの塔の解法を求める --- (*7)
result = []
def hanoi(n, src, des, temp):
    if n == 1: # 円盤が1つのとき
        result.append([src, des])
    else: # 円盤が2つ以上のとき
        hanoi(n - 1, src, temp, des)
        result.append([src, des])
        hanoi(n - 1, temp, des, src)
hanoi(5, 0, 2, 1) # 円盤が5枚のとき、柱番号で0番から2番へ移動することを指定

# 次の手順を描画 --- (*8)
def next_step(e):
    global result
    if len(result) == 0: return
    [src, des] = result[0] # ハノイの塔の解法を1つ取り出す
    result = result[1:] # 取り出したので先頭を削除
    labels = ['A', 'B', 'C'] # ウィンドウのタイトルに解法を表示
    win.title(f'{labels[src]} → {labels[des]}')
    cols[des].insert(0, cols[src][0]) # 柱の状態を更新
    cols[src] = cols[src][1:]
    draw_pillars() # 柱を描画

# マウスのクリックイベントでステップを進める --- (*9)
win.bind('<Button-1>', next_step)
draw_pillars() # 初期画面描画
win.mainloop() # ウィンドウのメインループを開始
