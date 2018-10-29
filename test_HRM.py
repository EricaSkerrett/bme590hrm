import pytest
import numpy as np
import json
from HRM import show_dir
from HRM import read_files
from HRM import extremes
from HRM import find_duration
from HRM import make_tuple
from HRM import filter
from HRM import find_peaks
from HRM import find_mean_HR
from HRM import make_dict
from HRM import make_json


# @pytest.mark.parametrize("candidate, expected" [
#    (8, TypeError),
#    ])
# def test_show_dir(candidate, expected):
#    with pytest.raises(expected):
#        mshow_dir(candidate)


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


def test_filter():  # specific to current filter settings
     a = [1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1]
     b = filter(a)
     c = sum(b)
     assert c == 84.85787742621548


def test_find_peaks():
    x = np.asarray([0, 1, 2, 3, 4, 5, 4, 3, 2, 1])
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    (a, b) = find_peaks(x, y)
    assert a == [6]


def test_find_mean_HR():
    a = 3
    b = np.asarray([1, 2, 3, 4, 5, 6])
    (x, y) = find_mean_HR(a, b)
    assert x == b.size/a*60


def test_make_dict():
    p1 = ['file1', 'file2']
    p2 = 10  # mean hr
    p3 = (0, 15)  # extremes tuple
    p4 = 10.5  # time duration
    p5 = 30  # numb beats
    p6 = np.asarray([1, 2, 3, 4])
    x = make_dict(p1, p2, p3, p4, p5, p6)
    y = dict([
        ('File_Name', p1[0]),
        ('Mean_HR_(BPM)', p2),
        ('Voltage_Extremes', p3),
        ('Data_Duration', p4),
        ('Number_Beats', p5),
        ('Time_of_Beats', p6.tolist()),
    ])
    assert x == y


# def test_make_json():
