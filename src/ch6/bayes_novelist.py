import naive_bayes as nb
import re
# 青空文庫の小説データを読み込みリストで返す --- (*1)
def read_novel(fname, author):
    with open(fname, 'rt', encoding='sjis') as fp:
        txt = fp.read()
    # ルビや注意書きを削除 --- (*2)
    txt = re.sub(r'《.*?》', '', txt)
    txt = re.sub(r'［.*?］', '', txt)
    # 最初の1万字を取り出す --- (*3)
    txt = txt if len(txt) < 10000 else txt[0:10000]
    # 改行で区切って学習用データを作る --- (*4)
    result = []
    for line in txt.split('\r\n'):
        line = line.strip()
        if len(line) < 5: continue
        result.append(line)
    return result, [author] * len(result)

nb.init_params()
# 小説データの前半を学習する --- (*5)
kokoro, soseki = read_novel('text/kokoro.txt', '夏目漱石')
nb.fit(kokoro, soseki)
maihime, ougai = read_novel('text/maihime.txt', '森鴎外')
nb.fit(maihime, ougai)
# 作品の後半を読み込ませて誰の作品か推測する --- (*6)
print('a:', nb.predict('始めて先生の宅を訪ねた時、先生は留守であった。二度目に行ったのは次の日曜だと覚えている。'))
print('b:', nb.predict('余ははじめて病牀に侍するエリスを見て、その変わりたる姿に驚きぬ。彼はこの数週のうちにいたく痩せて、血走りし目はくぼみ、灰色の頬は落ちたり。'))
