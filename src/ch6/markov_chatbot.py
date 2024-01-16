import random, re
from janome.tokenizer import Tokenizer
import markov, markov_chatbot_param as param
BOT_NAME = 'エリー' # チャットボットの名前 --- (*1)
tokenizer = Tokenizer()
# チャットボットの会話を生成する --- (*2)
def compose_response(question, dic):
    question = re.sub(r'[?？]', '。', question.strip())
    if '。' not in question: question += '。'
    # 定型フレーズがあればそれを返す ---- (*3)
    if question in param.PHRASES:
        return random.choice(param.PHRASES[question])
    # 形態素解析してキーワードを探す --- (*4)
    tokens = tokenizer.tokenize(question)
    keywords = []
    for w in tokens:
        p = (w.part_of_speech + '   ')[0:3]
        if '名詞,' in p or '形容詞' in p:
            keywords.append(w.base_form)
    # キーワードが全く見当たらないとき、辞書に登録して定型句を返す --- (*5)
    if len(keywords) == 0:
        markov.make_dictionary(question, dic)
        return random.choice(param.PHRASES['そうですね。'])
    # 関連キーワードをランダムに決める --- (*6)
    key = random.choice(keywords)
    # マルコフ辞書にキーワードがなければユーザーに意味を尋ねる --- (*7)
    if key not in dic['@']:
        print(f'{BOT_NAME}: 「{key}」ですか？それについて教えてください。')
        user = input('>>> ')
        if user == '': return '他に問題はありませんか？'
        if key not in user: user = key + 'は' + user
        if '。' not in user: user += '。'
        markov.make_dictionary(user, dic) # マルコフ辞書に登録
        return 'ありがとうございます。それでどうするんですか？'
    # キーワードから始まる文章を自動生成 --- (*8)
    top = dic['@']
    w1 = markov.choice_word(top[key])
    text = markov.compose_from_words(dic, key, w1)
    return text + random.choice(['どう思いますか？', 'それでどうしますか？'])

if __name__ == '__main__':
    dic = param.load_dic() # マルコフ辞書をファイルから読み込む --- (*9)
    print(f'{BOT_NAME}: {BOT_NAME}の部屋へようこそ！こんにちは。')
    while True: # 繰り返し会話と応答を繰り返す
        question = input('>>> ')
        if question == '' or question == 'さようなら': break
        answer = compose_response(question, dic)
        print(f'{BOT_NAME}: {answer}')
    # 別れの挨拶をして最後にファイルに辞書を保存 --- (*10)
    print(f'{BOT_NAME}: さようなら。また来てください！')
    param.save_dirc(dic)
