import os
# 全ファイル列挙 --- (*1)
def enumfiles(path):
    if os.path.isdir(path):
        # ディレクトリの場合
        for f in os.listdir(path):
            ff = os.path.join(path, f)
            enumfiles(ff) # 再帰的に処理 --- (*2)
    else:
        # ファイルの場合Excelファイルか判定 --- (*3)
        if path.endswith('.xls') or path.endswith('.xlsx'):
            print(path) # 表示

if __name__ == '__main__':
    # 指定ディレクトリ以下の全ファイルを列挙 --- (*4)
    enumfiles('./test_dir')

