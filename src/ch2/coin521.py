AMOUNT = 521
pattern = 0
for c1 in range(0, AMOUNT+1):
    for c5 in range(0, AMOUNT//5+1):
        for c10 in range(0, AMOUNT//10+1):
            for c50 in range(0, AMOUNT//50+1):
                for c100 in range(0, AMOUNT//100+1):
                    for c500 in range(0, AMOUNT//500+1):
                        total = c500*500 + c100*100 + c50*50 + c10*10 + c5*5 + c1
                        if total == AMOUNT:
                            pattern += 1
                            if pattern % 10 == 9:
                                print('(経過) 組合せ数=', pattern)
print('(結果) 組合せ数=', pattern)
