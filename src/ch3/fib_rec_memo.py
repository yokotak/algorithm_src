# fib関数の実行結果を覚えておくための辞書型変数 --- (*1)
fib_memo = {}
# 再帰的にフィボナッチ数を計算する関数
def fib(n):
    if n <= 1: return 1
    # 既に計算済みか確認 --- (*2)
    if n in fib_memo:
        return fib_memo[n]
    # 再帰的に関数fibを呼び出して、変数に結果を保存 --- (*3)
    fib_memo[n] = fib(n - 2) + fib(n - 1)
    return fib_memo[n]

# n個のフィボナッチ数列を求める関数
def fib_list(n):
    return [fib(i) for i in range(0, n)]

if __name__ == '__main__':
    # フィボナッチ数列を38個表示する
    print(fib_list(38))

