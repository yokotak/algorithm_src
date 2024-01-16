import sys
import caesar

# コマンドライン引数の数を確認 --- (*1)
if len(sys.argv) < 3:
    print('[使い方] caesar_cli.py "文章" (key_no)')
    quit()
# コマンドライン引数を取得 --- (*2)
src = sys.argv[1] # 文章
key_no = int(sys.argv[2]) # 何文字ずらすか
# 暗号化 --- (*3)
print(caesar.encrypt(src, key_no))

