# リングバッファを初期化 --- (*1)
def ringbuffer_new(size):
    return {
        'head': 0, # 先頭
        'tail': 0, # 末尾
        'size': 0, # 実際のサイズ
        'buffer': [0 for _ in range(size)] # バッファ
    }

# リングバッファに値を追加 --- (*2)
def ringbuffer_write(rb, v):
    # 書き込み
    rb['buffer'][rb['tail']] = v
    # 次回書き込み先を後ろに移動 --- (*3)
    rb['tail'] = (rb['tail'] + 1) % len(rb['buffer'])
    # バッファがいっぱいになったか --- (*4)
    if rb['size'] >= len(rb['buffer']):
        rb['head'] = (rb['head'] + 1) % len(rb['buffer'])
    else:
        rb['size'] += 1

# リングバッファから値を取得 --- (*5)
def ringbuffer_read(rb):
    if rb['size'] <= 0:
        return None
    v = rb['buffer'][rb['head']]
    rb['size'] -= 1
    # 読み取り位置を後ろに移動 --- (*6)
    rb['head'] = (rb['head'] + 1) % len(rb['buffer'])
    return v

# リングバッファのテスト --- (*7)
def test_ringbuffer1():
    # リングバッファを作成 --- (*8)
    rb = ringbuffer_new(3)
    # リングバッファに追加
    ringbuffer_write(rb, 0)
    ringbuffer_write(rb, 1)
    ringbuffer_write(rb, 2)
    assert ringbuffer_read(rb) == 0
    assert ringbuffer_read(rb) == 1
    assert ringbuffer_read(rb) == 2

# リングバッファのテスト(その2) --- (*9)
def test_ringbuffer2():
    rb = ringbuffer_new(3)
    # 1から100まで書き込む --- (*10)
    for i in range(1, 100+1):
        ringbuffer_write(rb, i)
    assert ringbuffer_read(rb) == 98
    assert ringbuffer_read(rb) == 99
    assert ringbuffer_read(rb) == 100
    assert ringbuffer_read(rb) is None

