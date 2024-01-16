import json
# ハフマン圧縮する関数 --- (*1)
def huffman_encode(data):
    # 文字の出現回数を数える --- (*2)
    count_dict = { c: data.count(c) for c in data }
    print('出現回数:', count_dict)
    # 末端のノードを生成する --- (*3)
    nodes = []
    for key, cnt in count_dict.items():
        node = {'key': key, 'count': cnt, 'left': None, 'right': None}
        nodes.append(node)
    # 出現回数を基にしてハフマン木を構築 --- (*4)
    while len(nodes) >= 2:
        # 最も小さな出現回数を持つノードを2つ取得 --- (*5)
        left = min(nodes, key=lambda o: o['count'])
        nodes.remove(left)
        right = min(nodes, key=lambda o: o['count'])
        nodes.remove(right)
        # 節となるノードを作る --- (*6)
        parent = {'key': None, 'count': left['count'] + right['count'],
            'left': left, 'right': right}
        # ノードリストに追加
        nodes.append(parent)
    # 先頭の要素がハフマン木のルートとなる
    tree = nodes[0]
    print('ハフマン木', json.dumps(tree, indent=2))
    # ハフマン木を基にして、2進数データを生成 --- (*7)
    code_dict = generate_code_dict({}, tree, '')
    bindata = ''
    for ch in data:
        bindata += code_dict[ch]
    return bindata, code_dict

# ハフマン木を元にした辞書を再帰的に生成 --- (*8)
def generate_code_dict(code_dict, node, binstr):
    if node is None:
        return
    if node['key'] is not None:
        code_dict[node['key']] = binstr
        return
    generate_code_dict(code_dict, node['left'], binstr + '0')
    generate_code_dict(code_dict, node['right'], binstr + '1')
    return code_dict

if __name__ == '__main__':
    # ハフマン符号化のテスト --- (*9)
    binstr, code_dict = huffman_encode('BCAADDDCCACACAC')
    print(f'ハフマン木の辞書: {code_dict}')
    print(f'エンコード: {binstr} ({len(binstr)}ビット)')
