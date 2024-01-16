from janome.tokenizer import Tokenizer
import random, re
tokenizer = Tokenizer() # 形態素解析の準備

# 文章を分割してマルコフ辞書に登録する --- (*1)
def make_dictionary(text, dic={}):
    # 形態素解析 --- (*2)
    wlist = [w.surface for w in tokenizer.tokenize(text)]
    # 形態素を辞書に登録 --- (*3)
    tmp = ['@'] # 文頭を表す記号
    for w in wlist:
        if w == '': continue
        tmp.append(w)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp.pop(0)
        w1, w2, w3 = tmp # 単語を3つ得て辞書に登録 --- (*4)
        if w1 not in dic: dic[w1] = {}
        if w2 not in dic[w1]: dic[w1][w2] = {}
        if w3 not in dic[w1][w2]: dic[w1][w2][w3] = 0
        if w == '。': # 文末に到達したら文頭をセット
            tmp = ['@']
            continue
    return dic
# マルコフ辞書を元にして作文する関数 --- (*5)
def compose(dic):
    top = dic['@'] # 文頭を選択 --- (*6)
    w1 = choice_word(top) # 文頭に続く単語を選ぶ
    w2 = choice_word(top[w1])
    return compose_from_words(dic, w1, w2)
# 文末に至るまで繰り返し語句を選び続ける --- (*7)
def compose_from_words(dic, w1, w2):
    ret = [w1, w2]
    while True:
        w3 = choice_word(dic[w1][w2])
        ret.append(w3)
        if w3 == '。': break
        w1, w2 = w2, w3
    return ''.join(ret)
# 辞書から選択肢を選ぶ --- (*8)
def choice_word(o):
    if type(o) is not dict: return '。'
    ks = list(o.keys()) # 辞書の子キー一覧を得る
    if len(ks) == 0: return '。'
    return random.choice(ks) # 辞書から選択肢を返す

if __name__ == '__main__':
    # 小説「こころ」を読んで先頭の1万字を辞書にする --- (*9)
    text = open('text/kokoro.txt', 'r', encoding='sjis').read()[0:10000]
    text = re.sub(r'(《.*?》|［.*?］)', '', text) # 不要な部分を削る
    text = re.sub(r'[｜\s\u3000\-]', '', text)
    # 文章をマルコフ辞書に登録し、作文する --- (*10)
    dic = make_dictionary(text)
    print(compose(dic))
