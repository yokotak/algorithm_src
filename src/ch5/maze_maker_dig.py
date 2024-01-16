import random, maze_draw
# 穴掘り法で迷路を作成する関数 --- (*1)
def make_maze(columns, rows):
    # 全てが壁(1)のrows×columnsの迷路を作る --- (*2)
    maze = [[1] * columns for _ in range(rows)]
    # 起点に通路を指定 --- (*3)
    maze[1][1] = 0
    # 迷路を掘り進む --- (*4)
    dig_maze(maze, 1, 1, columns, rows)
    return maze

# 再帰的に迷路を掘り進む関数 --- (*5)
def dig_maze(maze, x, y, columns, rows):
    # 上下左右を表すリスト --- (*6)
    udlr = [[0,-1],[0,1],[-1,0],[1,0]]
    # 上下左右をシャッフル
    random.shuffle(udlr)
    # 順に掘り進められるかを調べて2マス掘り進む --- (*7)
    for d in udlr:
        dx, dy = d
        x1, y1 = x+dx*1, y+dy*1 # 1マス先
        x2, y2 = x+dx*2, y+dy*2 # 2マス先
        # 範囲外か確認 --- (*8)
        if x2 < 0 or x2 >= columns-1: continue
        if y2 < 0 or y2 >= rows-1: continue
        # 2マス先が道か確認 --- (*9)
        if maze[y2][x2] == 0: continue
        # 穴を掘り進める --- (*10)
        maze[y1][x1] = 0
        maze[y2][x2] = 0
        # 再帰的に掘る --- (*11)
        dig_maze(maze, x2, y2, columns, rows)

if __name__ == '__main__': # --- (*12)
    maze = make_maze(41, 31)
    maze_draw.draw(maze, 'maze_maker_dig.png')

