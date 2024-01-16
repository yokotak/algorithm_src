import sys
import uesugi

# コマンドライン引数を処理 --- (*13)
if len(sys.argv) < 3:
    print('[使い方] uesugi_cli.py (暗号|復号) "文字列"')
    quit()
# コマンドライン引数を取得 --- (*14)
method = sys.argv[1]
src = sys.argv[2]
if method == '暗号' or method == 'e':
    print(uesugi.encrypt(src))
else:
    print(uesugi.decrypt(src))

