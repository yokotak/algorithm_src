import perfplot
import random
import bubblesort, combsort, selectionsort, insertionsort
import mergesort, shellsort, heapsort, quicksort

# 指定個数のランダムな数値を生成する関数
def make_samples(n):
    a = [random.randint(0, 10000) for _ in range(n)]
    print(f'test {n}=', a)
    return a

pp = perfplot.live(
    setup=lambda n: make_samples(n),
    n_range=range(0, 1000, 100), # 0から900までの値でテストする
    kernels=[
        # テストしたい関数を以下に列挙する
        bubblesort.bubblesort,
        selectionsort.selsort,
        combsort.combsort,
        insertionsort.insertion_sort,
        mergesort.mergesort,
        shellsort.shellsort,
        heapsort.heapsort,
        quicksort.quicksort,
    ]
)
