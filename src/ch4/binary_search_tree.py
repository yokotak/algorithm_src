# リストから二分探索木を構築 --- (*1)
def bstree_build(a):
    bsnode = lambda v, i: { 'value': v, 'index': i, 'left': None, 'right': None }
    root = bsnode(a[0], 0) # ルートを作成 --- (*2)
    if len(a) > 1:
        for i, v in enumerate(a[1:]): # ルートに子を追加していく
            bstree_insert(root, bsnode(v, i + 1))
    return root

# 二分探索木に値を追加 --- (*3)
def bstree_insert(node, v):
    # ノードの値と挿入したい値を比較
    if node['value'] < v['value']:
        if node['right'] is None: # ノードの右に追加
            node['right'] = v
        else:
            bstree_insert(node['right'], v)
    else:
        if node['left'] is None: # ノードの左に追加
            node['left'] = v
        else:
            bstree_insert(node['left'], v)

# 二分探索木nodeからvalueを検索 --- (*4)
def bstree_search(node, value):
    if node is None: # 木の末端に至ったら値は存在しない
        return None
    if node['value'] == value: # 値を見つけた
        print('- 発見!')
        return node
    if node['value'] > value: # ノードと値を比較
        print(f'- {node["value"]} > {value}')
        return bstree_search(node['left'], value) # 左を探す
    else:
        print(f'- {node["value"]} < {value}')
        return bstree_search(node['right'], value) # 右を探す

# テスト --- (*5)
def test_bstree():
    tree = bstree_build([1, 9, 8, 2, 3, 4, 5, 7, 6])
    assert bstree_search(tree, 8)['index'] == 2

if __name__ == '__main__':
    import json
    # 二分探索木を構築 --- (*6)
    tree = bstree_build([11, 15, 8, -3, 21, 12])
    print('tree=', json.dumps(tree, indent=2))
    # 木から21を検索 --- (*7)
    r = bstree_search(tree, 21)
    print('index=', r['index'], 'value=', r['value'])
