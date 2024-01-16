import ls_distance

# 辞書ファイルの指定 --- (*1)
DICT_FILE = 'ejdict-hand-utf8.txt'
words = {} # 辞書データを保持する辞書型変数

# 辞書ファイルの内容を読み込む --- (*2)
def read_dict_file():
    with open(DICT_FILE, 'rt', encoding='utf-8') as fp:
        for line in fp:
            word, mean = line.split('\t')
            # 長い日本語の説明文があればカットする --- (*2a)
            words[word] = mean[0:20]+'...' if len(mean) > 20 else mean

# 英単語を調べてスペルチェックをする --- (*3)
def spellcheck(word):
    if words == {}: read_dict_file()
    # 完全一致すればOKと表示 --- (*4)
    if word in words:
        print('[OK]', words[word])
        return
    # レーベンシュタイン距離を利用して候補を表示 --- (*5)
    for w, m in words.items():
        dist = ls_distance.calc_distance(word, w)
        if dist <= 1:
            print(f'[候補] {w} : {m}')

if __name__ == '__main__':
    # 繰り返し英単語の入力を求める --- (*6)
    while True:
        word = input('英単語を入力: ')
        if word == '': break
        print('---', word, '---')
        spellcheck(word)

