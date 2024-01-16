# 都市間の電車の運賃を定義したもの --- (*1)
fare_graph = {
    'A': {'B': 200, 'C': 170, 'D': 170},
    'B': {'F': 300},
    'C': {'E': 120},
    'D': {'E': 150},
    'E': {'F': 150},
}

# 深さ優先探索で最小運賃コストを調べる関数 --- (*2)
def dfs(city, visited, cost):
    if city in visited:  # 訪問済みか？
        return -1, None
    # 訪問済みにする --- (*3)
    visited.append(city)
    if city == 'F':  # 目的地に到着したら終了 --- (*4)
        print(f'到着: {visited} → {cost}円')
        return cost, visited
    # 探索可能な路線を全て計算して最小コストを調べる --- (*5)
    min_cost = -1
    min_visited = None
    for next_city, fare in fare_graph[city].items():
        # 再帰的にコストを計算する --- (*6)
        a_cost, a_visited = dfs(next_city, visited.copy(), cost + fare)
        if a_cost == -1:
            continue
        # 最小コストを更新する --- (*7)
        if min_cost == -1 or min_cost > a_cost:
            min_cost = a_cost
            min_visited = a_visited
    return min_cost, min_visited

if __name__ == '__main__':
    # 最小運賃コストを調べる --- (*8)
    min_fare, min_path = dfs('A', [], 0)
    print(f'最小運賃コスト: {min_fare}円')
    print(f'最小運賃コストの経路: {min_path}')

