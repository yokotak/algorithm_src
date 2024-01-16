import random
# トランプ生成のための定数
MARKS = ['♥','♦','♠','♣']
NUMS = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# カードを生成
for i in range(0, 4):
    line1 = ''
    line2 = ''
    for n in range(0, 13):
        no = i * 13 + n
        mark = MARKS[i]
        num = NUMS[n]
        line1 += str(no) + '\t'
        line2 += mark + num + '\t'
    print(line1)
    print(line2)


