import pytest
from HRM import make_dir
from HRM import read_files
from HRM import extremes
from HRM import duration

# @pytest.mark.parametrize("candidate, expected" [
#    (8, TypeError),
#    ])
# def test_make_dir(candidate, expected):
#    with pytest.raises(expected):
#        make_dir(candidate)


# @pytest.mark.parametrize("candidate, expected" [
#    ([], IndexError),
#    ])
# def test_read_files(candidate, expected):
#    with pytest.raises(expected):
#        read_files(candidate)


def test_extremes():
    x = [1, 2, 3]
    (y, z) = extremes(x)
    assert (y, z) == (3, 1)


def test_duration():
    x = 5
    y = 3
    z = duration(x, y)
    assert z == 2
