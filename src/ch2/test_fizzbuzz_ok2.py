# FizzBuzzの結果を返す関数(改良版)
def get_fizzbuzz(num):
    # FizzBuzz判定のために3と5で割った余りを最初に計算する
    is_fizz = (num % 3 == 0)
    is_buzz = (num % 5 == 0)
    # 上記の値を元にして順次判定を行う
    if is_fizz and is_buzz: return 'FizzBuzz'
    if is_fizz: return 'Fizz'
    if is_buzz: return 'Buzz'
    return str(num)

