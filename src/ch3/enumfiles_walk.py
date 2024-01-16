import os
def enumfiles(path):
    # os.walkでサブディレクトリ以下も全部取得
    for pathname, dirnames, filenames in os.walk(path):
        for f in filenames:
            ff = os.path.join(pathname, f)
            print(ff)

if __name__ == '__main__':
    # 指定ディレクトリ以下の全ファイルを列挙
    enumfiles('./test_dir')

