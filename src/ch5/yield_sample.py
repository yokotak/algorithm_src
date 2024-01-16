# yieldを使った関数の定義 --- (*1)
def get_proverb():
    yield '1.穏やかな舌は命の木である。'
    yield '2.悪意ある言葉は人を落胆させる。'

# forを使って関数get_proverbを呼び出す --- (*2)
for msg in get_proverb():
    print('[for]', msg)

# forを使わずに、関数get_proverbを呼び出す --- (*3)
g = get_proverb()
print('[next]', next(g))
print('[next]', next(g))
