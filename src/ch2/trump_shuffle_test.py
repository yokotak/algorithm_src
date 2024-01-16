import trump_shuffle as ts
import json, random

def test_trump_shuffle():
    for i in range(100):
        r = random.randint(0, 100)
        assert (0 <= r <= 100) == True
    arr = [1,2,3,4,5,6,7,8,9,10]
    ts.shuffle(arr)
    assert json.dumps(arr) != json.dumps([1,2,3,4,5,6,7,8,9,10])

