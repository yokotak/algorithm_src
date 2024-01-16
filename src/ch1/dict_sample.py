# 辞書型変数を初期化
fruits = {
  'Orange': 300,
  'Banana': 500,
  'Mango': 700
}
# 値を参照する
print( fruits['Banana'] ) # 結果: 500
# 値を更新する
fruits['Banana'] = 530
print( fruits['Banana'] ) # 結果: 530
# 値が存在するか確認
if 'Apple' in fruits:
    print('Appleが存在する')
else:
    print('Appleは存在しない')
