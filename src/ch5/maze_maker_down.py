import random, maze_draw

# 棒倒し法で迷路を作成する関数 --- (*1)
def make_maze(columns, rows):
    # 全てが通路(0)のrows×columnsの迷路を作る --- (*2)
    maze = [[0] * columns for _ in range(rows)]
    # 外周を壁にする --- (*3)
    for y in range(rows):
        maze[y][0] = 1
        maze[y][columns-1] = 1
    for x in range(columns):
        maze[0][x] = 1
        maze[rows-1][x] = 1
    # 1マスおきに上下左右のいずれかに壁を作成する --- (*3)
    for y in range(2, rows-2):
        for x in range(2, columns-2):
            if (x % 2 == 1)or(y % 2 == 1): # 1マスおきになるように
                continue
            maze[y][x] = 1 # 壁を配置
            # 上下左右の方向を表す座標を[x,y]で定義 --- (*4)
            udlr = [[0,-1],[0,1],[-1,0],[1,0]]
            # 2段目以降なら上に倒さない
            if y > 2: udlr.pop(0)
            # 上下左右の座標をシャッフルして壁があるか調べる --- (*5)
            random.shuffle(udlr)
            for d in udlr:
                dx, dy = d # 相対座標
                # 壁がなければ壁を作る --- (*6)
                if maze[y+dy][x+dx] == 0:
                    maze[y+dy][x+dx] = 1
                    break
    return maze

if __name__ == '__main__': # 迷路を作って画像で保存 --- (*7)
    maze = make_maze(41, 31)
    maze_draw.draw(maze, 'maze_maker_down.png')
