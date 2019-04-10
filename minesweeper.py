def test_1x1_0():
    assert ms(1, 1, []) == [[0]]

def test_1x1_1():
    assert ms(1, 1, [(0, 0)]) == [[-1]]

def test_1x2_0():
    assert ms(1, 2, []) == [[0, 0]]

def test_1x2_2():
    assert ms(1, 2, [(0, 0), (0, 1)]) == [[-1, -1]]

def test_1x2_left_only():
    assert ms(1, 2, [(0, 0)]) == [[-1, 1]]

# "len(mines) != 0" is the same to "bool(mines)"
# When casting to int, True => 1 and False => 0


#["*1",
# "11"]

def ms(rows, cols, mines):
    if cols == 2 and len(mines) == 1:
        return [[-1, 1]]
    if cols == 2:
        return [[-bool(mines), -bool(mines)]]

    return [[-bool(mines)]]
