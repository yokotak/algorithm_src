# FizzBuzz問題の結果を返す関数(完成版)

# FizzBuzzの結果を返す関数 --- (*1)
def get_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)

# get_fizzbuzzをテストする関数 --- (*2)
def test_get_fizzbuzz():
    assert get_fizzbuzz(3) == 'Fizz'
    assert get_fizzbuzz(7) == '7'
    assert get_fizzbuzz(15) == 'FizzBuzz'
    assert get_fizzbuzz(25) == 'Buzz'

