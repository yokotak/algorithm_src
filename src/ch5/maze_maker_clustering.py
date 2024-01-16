import random
import maze_draw
# クラスタリング法で迷路を作成する関数 --- (*1)
def make_maze(columns, rows):
    # 全てが壁(値1)のrows×columnsの迷路を作る --- (*2)
    maze = [[1] * columns for _ in range(rows)]
    # 格子状に通路を配置
    room_y, room_x = rows // 2, columns // 2
    # 部屋と壁データを初期化 --- (*3)
    walls = []
    for y in range(room_y):
        for x in range(room_x):
            maze[y*2+1][x*2+1] = 0  # 迷路データに部屋を作成 --- (*3a)
            # 壁データ([部屋1座標, 部屋2座標])を追加 --- (*3b)
            if y != room_y-1:
                walls.append([(x, y), (x, y+1)])  # 部屋とその下の部屋の座標
            if x != room_x-1:
                walls.append([(x, y), (x+1, y)])  # 部屋とその右の部屋の座標
    # 迷路の通路部分を部屋に見立てて通し番号をつける --- (*4)
    rooms = [no for no in range(room_y*room_x)]
    # ランダムに壁を壊す -- (*5)
    random.shuffle(walls)
    for wall in walls:
        x1, y1 = wall[0]  # 部屋1の座標
        x2, y2 = wall[1]  # 部屋2の座標
        room1 = rooms[y1+x1*room_y]  # 部屋1の通し番号
        room2 = rooms[y2+x2*room_y]  # 部屋2の通し番号
        # 同じ部屋番号であれば壁は壊さない --- (*6)
        if room1 == room2:
            continue
        # 壁を壊す処理
        if x1 == x2:
            maze[y1*2+2][x1*2+1] = 0  # 下の壁を壊す
        else:
            maze[y1*2+1][x1*2+2] = 0  # 右の壁を壊す
        # 部屋をつなげて通し番号を合わせる --- (*7)
        if room1 > room2:
            room1, room2 = room2, room1
        # 部屋番号がroom1のものをroom2に書き換え
        for no in range(len(rooms)):
            if rooms[no] == room1:
                rooms[no] = room2
    return maze

if __name__ == '__main__':  # --- (*8)
    maze = make_maze(41, 31)
    maze_draw.draw(maze, 'maze_maker_clustering.png')
