import copy
# キューの初期化 --- (*1)
def queue_new(def_values):
    if type(def_values) != list:
        return [def_values]
    return copy.copy(def_values)

# キューに値を追加 --- (*2)
def queue_enqueue(queue, v):
    queue.append(v)

# キューから値を取り出す --- (*3)
def queue_dequeue(queue):
    if len(queue) == 0:
        return None
    value = queue[0]
    del queue[0]
    return value

# キューをテストする関数 --- (*4)
def test_queue():
    # キューを初期化
    q = queue_new([0, 1])
    # キューに値を追加
    queue_enqueue(q, 2)
    queue_enqueue(q, 3)
    # キューから値を取り出す
    assert queue_dequeue(q) == 0
    assert queue_dequeue(q) == 1
    assert queue_dequeue(q) == 2
