# ハノイの塔を再帰で解く関数 --- (*1)
def hanoi(n, source, destination, temp, level, memo):
    indent = ("│   " * level) + '├─── '
    pad = "    " * (3 - level) + ''
    print(f'{indent}hanoi({n}, {source}, {destination}, {temp}){pad}{memo}')
    if n == 1:
        # 円盤1枚なら対象を目的地に移動 --- (*2)
        move_disk(source, destination, indent, pad, f'[2]  ───── n=1なので直接移動')
    if n >= 2:
        # 円盤2枚以上の場合の処理 --- (*3)
        # nより上の円盤を再帰によって待避用の杭に移動 --- (*3a)
        hanoi(n - 1, source, temp, destination,
              level+1, f'[3]a ───── n={n}より上の円盤を待避')
        # n(一番下の円盤)を目的地に移動 --- (*3b)
        move_disk(source, destination, indent, pad,
                  f'[3]b ───── n={n}(一番下の円盤)を目的地に移動')
        # 先ほど待避用の杭に移動した円盤を再帰によって目的地に移動 --- (*3c)
        hanoi(n - 1, temp, destination, source,
              level+1, f'[3]c ───── n={n}の時待避した円盤を移動')

# 円盤の移動を表示する関数 --- (*4)
def move_disk(source, destination, indent, pad, memo=''):
    print(f'{indent}move_disk({source} → {destination}) {pad}{memo}')

if __name__ == '__main__':
    # 円盤が3枚の時の手順を表示する --- (*5)
    hanoi(3, 'A', 'C', 'B', 0, '[5]  ───── 最初')

