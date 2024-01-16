import knn

# 手書き数字画像のCSVファイルを読み込む関数 --- (*1)
def load_digits(filename):
    with open(filename, 'rt', encoding='utf-8') as fp:
        csv = fp.read() # ファイルから読み込む
    images, labels = [], []
    for line in csv.split('\n'): # 改行で区切って繰り返す
        if line == '': continue
        data = list(map(lambda x: int(x), line.split(',')))
        images.append(data[0:64]) # 画像データを追加
        labels.append(data[64]) # ラベルを追加
    return images, labels

if __name__ == '__main__':
    # 学習用のデータファイルとテスト用のデータファイルを読み込む --- (*2)
    train_x, train_y = load_digits('optdigits.tra') # 学習用
    test_x, test_y = load_digits('optdigits.tes') # テスト用
    # 数が多すぎると実行に時間がかかるのでサンプル数を減らす --- (*3)
    train_x, train_y = train_x[0:1500], train_y[0:1500]
    test_x, test_y = test_x[0:500], test_y[0:500]
    # 数字の判定を行う --- (*4)
    pred_y = knn.predict(train_x, train_y, test_x, k=5)
    # 正しく判定できたか検証する --- (*5)
    ok = 0
    for py, ty in zip(pred_y, test_y):
        ok += 1 if py == ty else 0
    print(f'ok={ok}/{len(pred_y)}')
    print('正解率=', ok / len(pred_y))
