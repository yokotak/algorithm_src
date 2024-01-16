import copy, json, maze_draw
# 迷路の値の意味を定義 --- (*1)
ROAD, WALL, CHECKED = (0, 1, 2)

# 幅優先探索で再帰的に迷路を探索 --- (*2)
def maze_search(maze, start_pos, goal_pos):
    pos_list = []
    # スタート地点を探索候補に追加
    pos_list.append([start_pos[0], start_pos[1], []])
    # 探索候補pos_listを一つずつ調べる --- (*3)
    while len(pos_list) > 0:
        # 今回調べる地点を取り出す --- (*4)
        cx, cy, route = pos_list.pop(0)
        # 探索済みにセット --- (*5)
        maze[cy][cx] = CHECKED
        route.append((cx, cy))
        # ゴール判定 --- (*6)
        gx, gy = goal_pos
        if (cx == gx) and (cy == gy):
            print(f'{len(route)-1}歩でゴールに到達')
            return route
        # 周囲を順に探索 --- (*7)
        UDLR = [[0,-1],[0,1],[-1,0],[1,0]] # 上下左右の座標
        for c in UDLR:
            nx, ny = cx+c[0], cy+c[1] # 探索先の座標 --- (*8)
            if maze[ny][nx] == ROAD:
                pos_list.append((nx, ny, route.copy()))
    return None

if __name__== '__main__':
    # テスト用の迷路を読み出して探索開始 --- (*9)
    maze = json.load(open('maze_test.json', 'r'))
    route = maze_search(copy.deepcopy(maze), (1, 1), (39, 29))
    if route is None:
        print('探索失敗'); quit()
    # 探索の様子を画像に保存 --- (*10)
    for (x, y) in route:
        maze[y][x] = CHECKED
    maze_draw.draw(maze, 'maze_search_bfs_goal.png')
