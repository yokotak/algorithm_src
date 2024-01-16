# リストの初期化 --- (*1)
a_list = [0, 1, 2]

# リストに要素を追加 --- (*2)
a_list.append(3)
a_list.append(4)

# リスト全体を表示 --- (*3)
print('(*3) 全体=', a_list) 

# リストの任意の要素を参照 --- (*4)
print('(*4) a_list[3]=', a_list[3])

# リストから要素を削除 --- (*5)
del a_list[2]
print('(*5) 2を削除=', a_list)

# 全ての要素を削除 --- (*6)
a_list.clear()
print('(*6) clear後の要素数=', len(a_list))

