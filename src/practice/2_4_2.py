def coin(pay):
    comb = []
    count = []
    for i_10 in range(31):
        for i_5 in range(21):
            for i in range(19):
                if pay == 10*i_10 + 5*i_5 + i:
                    count.append((i+i_5+i_10))
                    comb.append((i, i_5, i_10))
    print(f"総組み合わせ{len(count)}")
    return count, comb

def mix_coin_use(count, comb):
    for i in range(len(count)):
        if count[i] == min(count):
            print(f"少ない硬貨の組み合わせは{count[i]}枚, 10円: {comb[i][2]:>2}, 5円: {comb[i][1]:>2}, 1円: {comb[i][0]:>2}")

def max_coin_use(count, comb):
    for i in range(len(count)):
        if count[i] == max(count):
            print(f"多い硬貨の組み合わせは　{count[i]}枚, 10円: {comb[i][2]:>2}, 5円: {comb[i][1]:>2}, 1円: {comb[i][0]:>2}")

if __name__=="__main__":
    count, comb = coin(278)
    mix_coin_use(count, comb)
    max_coin_use(count, comb)
