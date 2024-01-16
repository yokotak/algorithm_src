import os
# 全ファイル列挙 --- (*1)
def enumfiles(path):
    if os.path.isdir(path):
        # ディレクトリの場合 --- (*2)
        for f in os.listdir(path):
            ff = os.path.join(path, f)
            enumfiles(ff) # 再帰的に処理 --- (*3)
    else:
        # ファイルの場合 --- (*4)
        print(path)

if __name__ == '__main__':
    # 指定ディレクトリ以下の全ファイルを列挙 --- (*5)
    enumfiles('./test_dir')

