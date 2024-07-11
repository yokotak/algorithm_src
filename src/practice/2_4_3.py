def coin(pay):
    count = 0
    y500 = pay//500 + 1
    y100 = pay//100 + 1
    y50 = pay//50 + 1
    y10 = pay//10 + 1
    y5 = pay//5 + 1

    for i_500 in range(y500):
        for i_100 in range(y100):
            for i_50 in range(y50):
                for i_10 in range(y10):
                    for i_5 in range(y5):
                        for i in range(pay+1):
                            sum = 500*i_500 + 100*i_100 + 50*i_50 + 10*i_10 + 5*i_5 + i
                            if pay == sum:
                                count += 1

    print(f"総組み合わせ{count}")
    return count

if __name__ == "__main__":
    coin(521)