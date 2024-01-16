# チャットボットのパラメーター
import json, os
# 定型をフレーズ --- (*1)
PHRASES = {
    'こんにちは。': ['お元気ですか？', '何かお困りですか？', 'これから何をしますか？'],
    '元気ですか。': ['変わらず元気です。あなたは？', '私は元気いっぱいです。あなたは？'],
    'そうですね。': ['それについて、もう少し詳しく教えてください。', 'それで、どうするんですか？']
}
# ファイルの保存先 --- (*2)
SAVE_FILE = './markov_chatlog.json'
# ファイルへの保存
def save_dic(dic):
    with open(SAVE_FILE, 'w') as fp:
        json.dump(dic, fp, ensure_ascii=False, indent=2)
# ファイルからデータを読み込む
def load_dic(savefile):
    dic = {'@':{}} # 辞書を初期化
    if os.path.exists(SAVE_FILE): # ファイルからデータを読み込む 
        with open(SAVE_FILE, 'r') as fp:
            return json.load(fp)
