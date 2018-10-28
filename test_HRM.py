import pytest
from HRM import make_dir
from HRM import read_files
from HRM import extremes
from HRM import find_duration
from HRM import make_tuple

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


def test_find_duration():
    x = 5
    y = 3
    z = find_duration(x, y)
    assert z == 2


def test__make_tuple():
    x = 1
    y = 2
    z = make_tuple(x, y)
    assert z == (1, 2)
