import maze_maker_clustering, maze_draw
import json

# 迷路を生成
maze = maze_maker_clustering.make_maze(41, 31)
# 迷路をJSONファイルに保存
json.dump(maze, open('maze_test.json', 'w'))
# 画像も保存
maze_draw.draw(maze, 'maze_maker_save_to_json.png')

