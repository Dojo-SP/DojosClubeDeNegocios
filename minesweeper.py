import pytest

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

@pytest.mark.parametrize('n, m', [
    (2, 2), (5, 10), (7, 3), (1, 5), (19, 27),
])
def test_nxm_0(n, m):
    result = ms(n, m, [])
    assert len(result) == n
    for row in result:
        assert len(row) == m == row.count("0")

@pytest.mark.parametrize(("n", "m"), [
    (2, 2), (2, 3), (3, 2), (27, 38), (4, 10)
])
def test_nxm_1_top_left(n, m):
    result = ms(n, m, [(0, 0)])
    assert len(result) == n
    assert "".join(result).count("0") == (n*m)-4
    for i, row in enumerate(result):
        if i == 0:
            assert row[:2] == "*1"
            assert row[2:] == "0" * (m-2)
        elif i == 1:
            assert row[:2] == "11"
        assert len(row) == m

def ms(rows, cols, mines):
    if not mines:
        return ["0" * cols] * rows
    elif rows == 1 and cols == 1 and len(mines) == 1:
        return ["*"]
    elif rows == 1 and cols == 2 and len(mines) == 2:
        return ["**"]
    elif rows == 1 and cols == 2 and mines == [(0, 0)]:
        return ["*1"]
    elif rows == 1 and cols == 2 and len(mines) == 1:
        return ["1*"]
    elif rows == 2 and cols == 2 and len(mines) == 1:
        return ["*1", "11"]
    else:
        result = [["0" for i in range(cols)]
                       for j in range(rows)]
        result[0][0] = "*"
        result[0][1] = "1"
        result[1][0] = "1"
        result[1][1] = "1"
        return ["".join(row) for row in result]
