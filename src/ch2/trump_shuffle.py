import random

# トランプのための定数 --- (*1)
MARKS = ['♥','♦','♠','♣']
NUMS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

def shuffle(arr): # シャッフル --- (*2)
    for i in reversed(range(1, len(arr))):
        k = random.randint(0, i)
        arr[i], arr[k] = arr[k], arr[i]

def get_card_label(no): # カードラベル --- (*3)
    mark = no // 13
    num = no % 13
    return MARKS[mark] + NUMS[num]

if __name__ == '__main__':
    # トランプをシャッフル --- (*4)
    cards = list(range(0, 52))
    shuffle(cards)
    # 先頭の7枚を表示 --- (*5)
    print([get_card_label(no) for no in cards[0:7]])
