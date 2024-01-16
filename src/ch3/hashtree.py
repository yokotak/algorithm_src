import hashlib
# ファイルのリストからハッシュ木を生成する関数 --- (*1)
def build_hashtree_from_files(files):
    nodes = []
    for i, file in enumerate(files):
        # ファイルを読んでハッシュ値を求めて空ノードを生成 --- (*2)
        with open(file, 'rb') as fp:
            data = fp.read().decode('utf-8')
        node = {'hash': get_hash(data), 'left': None, 'right': None}
        nodes.append(node)
    return build_hashtree_rec(nodes)

# ノードのリストからハッシュ木を生成する --- (*3)
def build_hashtree_rec(nodes):
    # 要素が奇数なら末尾をコピーして要素を偶数個にする --- (*4)
    if len(nodes) % 2 == 1:
        nodes.append(nodes[-1].copy())
    # 要素数が2つか --- (*5)
    if len(nodes) == 2:
        # 2つならそれが左右の子ノードとなる --- (*6)
        left, right = nodes[0], nodes[1]
    else:
        # リストの中央を調べる --- (*7)
        middle = len(nodes) // 2
        # 引数のnodesを左右分割して再帰的に呼び出す --- (*8)
        left = build_hashtree_rec(nodes[middle:])
        right = build_hashtree_rec(nodes[:middle])
    # 左右の子ノードから新たなハッシュを求める --- (*9)
    hash_v = get_hash(left['hash'] + right['hash'])
    return {'left': left, 'right': right, 'hash': hash_v}

# SHA-256でハッシュ値を求める --- (*10)
def get_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# 再帰的に全ノードを画面に出力 --- (*11)
def print_htree(node, level=0):
    indent = '┃  ' * level
    print(indent + '┣━ ' + node['hash'])
    if node['left'] is not None:
        print_htree(node['left'], level+1)
    if node['right'] is not None:
        print_htree(node['right'], level+1)

if __name__ == '__main__':
    # ファイルを指定してハッシュ木を生成して出力 --- (*12)
    htree = build_hashtree_from_files([
        'files/a.txt', 'files/b.txt',
        'files/c.txt', 'files/d.txt'])
    print_htree(htree)

