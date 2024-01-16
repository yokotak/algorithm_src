import perfplot
import random
import custom_sort, custom_sort_cache

def f_sort(a):
    a = a.copy()
    custom_sort.bsort(a, key=lambda o: o['price'])
    return True

def f_sort_cache(a):
    a = a.copy()
    custom_sort_cache.bsort(a, key=lambda o: o['price'])
    return True


# 指定個数のランダムな数値を生成する関数
def make_samples(n):
    a = [{'name': 'test', 'price': random.randint(0, 5000)} for _ in range(n)]
    print(f'test {n}=', a)
    return a

pp = perfplot.live(
    setup=lambda n: make_samples(n),
    n_range=range(10, 200, 20),
    kernels=[
        # テストしたい関数を以下に列挙する
        f_sort,
        f_sort_cache,
    ],
    labels=[
        'custom_sort',
        'custom_sort_cache',
    ]
)

