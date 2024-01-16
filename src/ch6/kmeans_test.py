import kmeans

def test_argmin():
    assert kmeans.argmin([1,2,3]) == 0
    assert kmeans.argmin([5,0]) == 1

def test_kmeans():
    # 2分割の場合
    data = [(0,0), (1,1), (1,0), (5,5),(4,5),(4,4)]
    ids = kmeans.kmeans(data, 2, 1000)
    assert ids == [0,0,0,1,1,1] or ids == [1,1,1,0,0,0]
    # 3分割の場合
    data = [(0,0), (1,1), (0,5), (1,5), (5,5), (4,4)]
    ids = kmeans.kmeans(data, 3, 1000)
    assert ids == [0,0,1,1,2,2] or ids == [1,1,0,0,2,2] or ids == [2,2,0,0,1,1] or ids == [2,2,1,1,0,0] or [1,1,2,2,0,0]
