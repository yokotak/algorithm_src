# def coin(pay):
#     comb = []
#     for i10 in range(31):
#         balance10 = pay - 10*i10
#         for i5 in range(10):
#             balance5 = balance10 - 5*i5
#             for i in range(12):
#                 balance = balance5 - i
#                 if balance == 0:
#                     comb.append((+i, i5, i10))
#                     # comb.append({"1y":i, "5y":i5, "10y":i10})

#     return comb

def coin(pay):
    for i_10 in range(31):
        for i_5 in range(10):
            for i in range(13):
                if pay == 10*i_10 + 5*i_5 + i:
                    print(f"10円: {i_10:>2}, 5円: {i_5:>2}, 1円: {i:>2}")

if __name__ == "__main__":
    coin(325)