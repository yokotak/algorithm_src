# 上杉暗号の変換テーブルを定義 --- (*1)
CONV_TABLE = [
    ['い','ろ','は','に','ほ','へ','と'],
    ['ち','り','ぬ','る','を','わ','か'],
    ['よ','た','れ','そ','つ','ね','な'],
    ['ら','む','う','ゐ','の','お','く'],
    ['や','ま','け','ふ','こ','え','て'],
    ['あ','さ','き','ゆ','め','み','し'],
    ['ゑ','ひ','も','せ','す','ん','○']
]

# 変換テーブル(二次元リスト)を辞書型に変換 --- (*2)
CONV_DIC = {}
for row, cols in enumerate(CONV_TABLE):
    for col, ch in enumerate(cols):
        CONV_DIC[ch] = f'{row+1}{col+1}'

if __name__ == '__main__':
    print(CONV_DIC) # 辞書型の様子を表示