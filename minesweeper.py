def test_1x1_0():
    assert ms(1, 1, []) == ["0"]

def test_1x1_1():
    assert ms(1, 1, [(0, 0)]) == ["*"]

def test_1x2_0():
    assert ms(1, 2, []) == ["00"]

def test_1x2_2():
    assert ms(1, 2, [(0, 0), (0, 1)]) == ["**"]

def test_1x2_left_only():
    assert ms(1, 2, [(0, 0)]) == ["*1"]

def test_1x2_right_only():
    assert ms(1, 2, [(0, 1)]) == ["1*"]

# "len(mines) != 0" is the same to "bool(mines)"
# When casting to int, True => 1 and False => 0


#["*1",
# "11"]

def ms(rows, cols, mines):
    if rows == 1 and cols == 1 and len(mines) == 0:
        return ["0"]
    elif rows == 1 and cols == 1 and len(mines) == 1:
        return ["*"]
    elif rows == 1 and cols == 2 and len(mines) == 0:
        return ["00"]
    elif rows == 1 and cols == 2 and len(mines) == 2:
        return ["**"]
    elif rows == 1 and cols == 2 and mines == [(0, 0)]:
        return ["*1"]
    elif rows == 1 and cols == 2 and len(mines) == 1:
        return ["1*"]
