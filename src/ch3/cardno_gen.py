from checkdigit import checkdigit

# 独自の会員番号の末尾にチェックディジットを加える
def add_checkdigit(numbers):
    # 0から9のいずれかを加えて確認する --- (*1)
    for no in range(10):
        cno = numbers + str(no)
        if checkdigit(cno):
            return cno
    return numbers + '?'

# 正しい会員番号を生成するかテスト --- (*2)
def test_add_checkdigit():
    assert add_checkdigit('1001') == '10017'
    assert add_checkdigit('356600202036050') == '3566002020360505'
    assert add_checkdigit('510510510510510') == '5105105105105100'
    assert add_checkdigit('37144963539843') == '371449635398431'


