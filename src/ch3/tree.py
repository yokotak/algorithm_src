import os, sys
# インデントに使う記号を宣言 --- (*1)
INDENT_PIN_C = '├── '
INDENT_PIN_E = '└── '
INDENT_BLANK = '    '
INDENT_LEVEL = '│   '
# 再帰的にファイル一覧を表示する関数 --- (*2)
def enumfiles(path, indent='', level=0, is_last=False):
    # ファイル(ディレクトリ)の先頭に表示する記号を選択 --- (*3)
    pin = INDENT_PIN_E if is_last else INDENT_PIN_C
    pin = '' if level == 0 else pin
    if os.path.isdir(path):
        # ディレクトリの場合 --- (*4)
        print(indent + pin + os.path.basename(path))
        # インデント記号を用意する --- (*5)
        indent += INDENT_BLANK if is_last else INDENT_LEVEL
        indent = '' if level == 0 else indent
        # ディレクトリ以下のファイル一覧を取得して繰り返す --- (*6)
        subdirs = list(sorted(os.listdir(path)))
        for i, f in enumerate(subdirs):
            ff = os.path.join(path, f)
            is_last = ((len(subdirs)-1) == i) # 最後の要素か --- (*7)
            enumfiles(ff, indent, level+1, is_last) # 再帰 --- (*8)
    else:
        # ファイルの場合 --- (*9)
        print(indent + pin + os.path.basename(path))

if __name__ == '__main__':
    # コマンドラインを解析 --- (*10)
    if len(sys.argv) < 2:
        print('USAGE: tree.py (path)')
        quit()
    enumfiles(sys.argv[1])
