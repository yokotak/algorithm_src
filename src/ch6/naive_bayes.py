from janome.tokenizer import Tokenizer
import math, pprint
tokenizer = Tokenizer()
# パラメータを初期化 --- (*1)
def init_params():
    global cat_words, cat_docs, cat_wc, doc_count
    cat_words = {} # カテゴリごとに{'単語':出現数}の辞書型のデータ
    cat_docs = {} # カテゴリごとの文章数
    cat_wc = {} # カテゴリごとの単語の出現回数
    doc_count = 0 # 学習したデータ数

# 文章を学習する --- (*2)
def fit(text_list, cat_list):
    global doc_count
    # カテゴリごとに語彙の出現回数を数える --- (*3)
    for text, cat in zip(text_list, cat_list):
        # カテゴリの文章数に1を加算 --- (*3a)
        cat_docs[cat] = cat_docs.get(cat, 0) + 1
        for tok in tokenizer.tokenize(text): # 形態素解析
            word = tok.base_form # 単語の基本形を得る --- (*3b)
            if cat not in cat_words: cat_words[cat] = {}
            # カテゴリにおける単語の出現回数に1を加算 --- (*3c)
            cat_words[cat][word] = cat_words[cat].get(word, 0) + 1
        doc_count += 1
    # カテゴリごとの単語の出現回数を数える --- (*4)
    for cat in cat_docs.keys():
        cat_wc[cat] = sum(cat_words[cat].values())

# 文章からカテゴリを予測する --- (*5)
def predict(text, debug=False):
    tokens = list(tokenizer.tokenize(text)) # 形態素解析
    # カテゴリごと出現単語をカウントして確率を計算 --- (*6)
    p = {}
    for cat, cat_num in cat_docs.items():
        p[cat] = math.log(cat_num / doc_count) # 初期値
        # カテゴリごとに単語の出現回数を数える --- (*7)
        for tok in tokens:
            word = tok.base_form # 単語の基本形を得る --- (*7a)
            wc = cat_words[cat].get(word, 0) + 1 # 単語の出現回数を数える --- (*7b)
            # カテゴリにおける確率を計算 --- (*7c)
            p[cat] += math.log(wc / cat_wc[cat])
    if debug: pprint.pprint(p)
    # ソートして最も可能性の高いものを返す --- (*8)
    pl = sorted(p.items(), key=lambda x: x[1], reverse=True)
    return pl[0][0]

if __name__ == '__main__':
    init_params() # パラメータの初期化 --- (*9)
    # 文章とカテゴリを指定して学習 --- (*10)
    fit(['恋は突然で愛は情熱的だ。世紀のロマンス'],['映画'])
    fit(['彼の投球は好調。チームはホームランを連発。'],['スポーツ'])
    fit(['Pythonでアルゴリズムを記述しよう。'],['プログラミング'])
    # 文章のカテゴリを予測 --- (*11)
    r = predict('アルゴリズムを勉強しよう。', debug=True)
    print('予測カテゴリ:', r)
