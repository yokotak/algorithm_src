# FizzBuzz問題の結果を返す関数(テストのみ)

# FizzBuzzの結果を返す関数(まだ空っぽ) --- (*1)
def get_fizzbuzz(num):
    return "FizzBuzz"

# get_fizzbuzzをテストする関数 --- (*2)
def test_get_fizzbuzz():
    assert get_fizzbuzz(3) == 'Fizz'
    assert get_fizzbuzz(7) == '7'
    assert get_fizzbuzz(15) == 'FizzBuzz'
    assert get_fizzbuzz(25) == 'Buzz'

