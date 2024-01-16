import random
# 初期値の指定 --- (*1)
UDLR = [[0,-1],[0,1],[-1,0],[1,0]]
INIT_LIST = [(n+1) % 16 for n in range(16)]
# 画面にデータを表示する --- (*2)
def show_data(data):
    data_s = map(lambda v: f'[{v:02d}]', data) # データを文字列に変換
    s = ''
    for i, v in enumerate(data_s):
        v = v if v != '[00]' else '[__]'
        s += (v + '\n') if i % 4 == 3 else v # 4つごとに改行をいれる
    print('---\n' + s + '---')
# dirの方向に穴を移動する --- (*3)
def move(data, dir):
    i1, i2 = calc_index(data, dir)
    data[i1], data[i2] = data[i2], data[i1]
# 移動先のインデックスを計算 --- (*4)
def calc_index(data, dir):
    i2 = i1 = data.index(0) # 穴の位置を得る
    y1, x1 = i1 // 4, i1 % 4 # 座標を確認
    y2, x2 = y1+dir[1], x1+dir[0] # 移動先を計算
    if 0 <= y2 <= 3 and 0 <= x2 <= 3: # 範囲なら穴を移動
        i2 = y2 * 4 + x2
    return i1, i2
# データをシャッフル --- (*5)
def shuffle_data(data, shuffle_time):
    for _ in range(shuffle_time):
        move(data, UDLR[random.randint(0, 3)])
# ゲームの初期化処理 --- (*6)
def init_game(shuffle_time):
    data = [INIT_LIST[i] for i in range(16)]
    shuffle_data(data, shuffle_time)
    show_data(data)
    return data
# ゲームの開始 --- (*7)
def start_game(data):
    while True:
        user_input(data)
        if data == INIT_LIST:
            print('clear!')
            quit()
# ユーザーからの入力に応じて穴を移動する --- (*8)
def user_input(data):
    s = input('穴の移動先: [0]上[1]下[2]左[3]右 > ')
    i = int(s) if (s != '') and (s in '0123') else -1
    if 0 <= i <= 3:
        move(data, UDLR[i])
        show_data(data)
if __name__ == '__main__': # --- (*9)
    start_game(init_game(8))

'''
【プログラムの解説】
(*1)では定数を初期化します。UDLRは上下左右の相対座標で、INIT_LISTは15パズルの正解配置を定義します。(*2)は画面にデータを表示する関数を定義します。(*3)は引数dirの方向に穴を移動する関数を定義します。なお、引数dirの値は上=0,下=1,左=2,右=3です。

(*4)は移動先のインデックスを計算する関数を定義します。(*5)はランダムに穴の位置を移動することでパズルデータシャッフルします。(*6)ではゲームの初期化処理を行います。

(*7)では繰り返しユーザーの操作に対応し、パズルが揃ったかを判定する処理を繰り返します。(*8)ではのユーザーからの入力値を得て、穴の位置を移動します。

最後の(*9)ではゲームを開始するため、関数start_gameを呼び出します。
'''
