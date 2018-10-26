import pytest
from HRM import make_dir
from HRM import read_files
# check that folder is there

@pytest.mark.parametrize("candidate, expected" [
    (8, TypeError),
    ])
def test_make_dir(candidate, expected):
    with pytest.raises(expected):
        make_dir(candidate)


@pytest.mark.parametrize("candidate, expected" [
    ([], IndexError),
    ])
def test_read_files(candidate, expected):
    with pytest.raises(expected):
        read_files(candidate)


# from HRM import open_files

# a = ['a.csv','b.csv','c.csv']
# b = ['a.csv','b.xyz','b.csv','c.csv']

# def test_read_files():
#  files = read_files()
# assert files == a
