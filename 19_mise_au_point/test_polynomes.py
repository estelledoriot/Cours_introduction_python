from polynomes import racines

assert racines(1, 0, 1) == []
assert racines(1, 0, 0) == [0.0]
assert racines(1, 0, -1) == [-1.0, 1.0]
