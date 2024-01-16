import os, sys
# 設定
MAX_LEVEL = 3 # 3階層以上のディレクトリの再帰を中止する
# インデントに使う記号を宣言
INDENT_PIN_C = '├── '
INDENT_PIN_E = '└── '
INDENT_BLANK = '    '
INDENT_LEVEL = '│   '
# 拡張子でアイコンを変える
ICONS = {
    'dir': '📁',
    'unknown': '❓',
    '.txt': '📄',
    '.zip': '🗄',
    '.xls': '📊',
    '.xlsx': '📊',
    '.py': '🐣',
}

# 再帰的にファイル一覧を表示する関数
def enumfiles(path, indent='', level=0, is_last=False):
    # ファイル(ディレクトリ)の先頭に表示する記号を選択
    pin = INDENT_PIN_E if is_last else INDENT_PIN_C
    pin = '' if level == 0 else pin
    if os.path.isdir(path):
        # ディレクトリの場合
        print(indent + pin + ICONS['dir'] + os.path.basename(path))
        # MAX_LEVEL階層以上ならそれ以上は省略する
        if level >= MAX_LEVEL:
            return
        # インデント記号を用意する
        indent += INDENT_BLANK if is_last else INDENT_LEVEL
        indent = '' if level == 0 else indent
        # ディレクトリ以下のファイル一覧を取得して繰り返す
        subdirs = os.listdir(path)
        # ただしドットから始まるファイルを省略する
        subdirs = filter(lambda f: not f.startswith('.'), subdirs)
        subdirs = list(sorted(subdirs))
        for i, f in enumerate(subdirs):
            ff = os.path.join(path, f)
            is_last = ((len(subdirs)-1) == i) # 最後の要素か
            enumfiles(ff, indent, level+1, is_last) # 再帰
    else:
        # ファイルの場合
        # 拡張子を得る
        _path, ext = os.path.splitext(path)
        icon = ICONS[ext] if ext in ICONS else ICONS['unknown']
        print(indent + pin + icon + os.path.basename(path))

if __name__ == '__main__':
    # コマンドラインを解析
    if len(sys.argv) < 2:
        print('USAGE: tree2.py (path)')
        quit()
    enumfiles(sys.argv[1])
