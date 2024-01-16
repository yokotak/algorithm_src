# 1からnまでの合計を求める関数
def rec_sum(n):
    # 1以下なら1を返す --- (*1)
    if n <= 1:
        return 1
    # 1からn-1までの合計を再帰的に求めnを足す --- (*2)
    return n + rec_sum(n - 1)

# 1から10までの合計を表示 --- (*3)
print(rec_sum(10))

