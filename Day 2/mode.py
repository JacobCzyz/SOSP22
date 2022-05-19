import statistics

def mode(list):
    if len(list) == 0:
        return None
    return statistics.mode(list)

def test_mode():
    assert mode([1, 1, 0]) == 1, "Simple basic case should give 1"
    assert mode([0, -342, -342]) == -342
    assert mode([-1, 4, 0, 0, 0, 0, 0]) == 0
    assert mode([42]) == 42, "Single number should return itself"
    assert mode([]) is None, "Empty list should give None" 