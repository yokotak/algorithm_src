import copy, json, maze_draw
# 迷路の値の意味を定義 --- (*1)
ROAD, WALL, CHECKED = (0, 1, 2)

# 深さ優先探索で再帰的に迷路を探索 --- (*2)
def maze_search(maze, cur_pos, goal_pos, level, route):
    # 現在座標を訪問済みにする --- (*3)
    cx, cy = cur_pos
    maze[cy][cx] = CHECKED
    route.append((cx, cy))
    # 現在位置がゴールか確認 ---- (*4)
    gx, gy = goal_pos
    if (cx == gx) and (cy == gy):
        print(f'{level}歩でゴール')
        return route
    # 周囲を順に探索 --- (*5)
    UDLR = [[0,-1],[0,1],[-1,0],[1,0]] # 上下左右の座標
    for c in UDLR:
        nx, ny = cx+c[0], cy+c[1] # 探索先の座標
        # 壁か探索済みならば続ける --- (*6)
        if (maze[ny][nx] == WALL) or (maze[ny][nx]) == CHECKED:
            continue
        # 再帰的に迷路を探索 --- (*7)
        r = maze_search(maze, (nx, ny), goal_pos, level+1, route.copy())
        if r is not None: return r # ゴールなら探索を終了
    return None

if __name__== '__main__':
    # テスト用の迷路を読み出す --- (*8)
    maze = json.load(open('maze_test.json', 'r'))
    # 迷路を探索 ---- (*9)
    route = maze_search(copy.deepcopy(maze), (1, 1), (39, 29), 0, [])
    if route is None:
        print('探索失敗'); quit()
    # 探索の様子を画像に保存 --- (*10)
    for (x, y) in route:
        maze[y][x] = CHECKED
    maze_draw.draw(maze, 'maze_search_dfs_goal.png')

