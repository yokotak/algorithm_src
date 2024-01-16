# 都市間の電車の運賃を定義したもの --- (*1)
fare_graph = {
    'A': {'B': 200, 'C': 170, 'D': 170},
    'B': {'F': 300},
    'C': {'E': 120},
    'D': {'E': 150},
    'E': {'F': 150},
}

# 深さ優先探索で最小運賃コストを求める関数 --- (*2)
def bfs():
    # 探索用のキューを準備
    queue = []
    # 初期値をキューに入れる
    queue.append({'city': 'A', 'visited': [], 'cost': 0})
    # キューが空になるまで繰り返す --- (*3)
    min_cost = -1
    min_visited = None
    while len(queue) > 0:
        # キューから取り出す --- (*4)
        it = queue.pop(0)
        city, visited, cost = it['city'], it['visited'], it['cost']
        # 訪問済みか？
        if city in visited:
            continue
        # 訪問済みにする --- (*5)
        visited.append(city)
        # 目的地に到着したか --- (*6)
        if city == 'F':
            print(f'到着: {visited} → {cost}円')
            # それが最小コストなら値を更新 --- (*7)
            if min_cost == -1 or min_cost > cost:
                min_cost = cost
                min_visited = visited
            continue
        # 探索可能な路線を全てキューに追加する --- (*8)
        for next_city, fare in fare_graph[city].items():
            queue.append({
                'city': next_city,
                'visited': visited.copy(),
                'cost': cost + fare
            })
    return min_cost, min_visited

if __name__ == '__main__':
    # 最小運賃コストを調べる --- (*9)
    min_fare, min_path = bfs()
    print(f'最小運賃コスト: {min_fare}円')
    print(f'最小運賃コストの経路: {min_path}')

