import os
import sys
import csv
import scipy
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

folder = "/users/esker/MedicalDeviceSoftware/bme590hrm/test_data/"
# User types in path to data folder


def main():
    dir = make_dir(folder)
    files = read_files(dir)
    csv_f = open_files(files)
    (time, volt, rawdata) = split_into_array(csv_f)
    (max_t, min_t) = extremes(time)
    (max_v, min_v) = extremes(volt)
    time_duration = duration(max_t, min_t)  # Time duration of ECG strip
    volt_extremes = make_tuple(max_v, min_v)  # Tuple of min and max voltages
    # extremes(volt)
    smooth_volt = filter(volt)
    (beats, peak_voltages) = find_peaks(smooth_volt, time)  # np arrays of
    mean_HR = find_mean_HR(time_duration, beats)
    # peak info
    # plt.show()


def make_dir(folder):
    if not isinstance(folder, str):
        raise TypeError("Path to folder with test data must "
                        "be entered as string")
    dir = os.listdir(folder)
    return(dir)


def read_files(dir):
    files = []
    for file in dir:
        if file.endswith('.csv'):
            files.append(file)
    sorted(files)  # trying to put it into numerical order but it's not working
    # print(files)
    if dir == []:
        raise IndexError("No .csv files present in folder")
    return(files)


def open_files(files):  # open just 1 file for now
    f = open(folder + files[0])
    csv_f = csv.reader(f)
    # print(csv_f)
    # print(files[0])
    return(csv_f)


def split_into_array(csv_f):
    time = []  # will eventually want to put these into a dictionary
    volt = []
    rawdata = []
    for i in csv_f:
        time.append((i[0]))
        volt.append(float(i[1]))
        rawdata.append([i[0], i[1]])
    volt = [float(i) for i in volt]
    time = [float(i) for i in time]
    return(time, volt, rawdata)


def extremes(x):
    max_x1 = max(x)
    min_x1 = min(x)
    max_x = float(max_x1)
    min_x = float(min_x1)
    # print(max_x)
    # print(min_x)
    return(max_x, min_x)


def duration(x, y):
    diff = x - y
    return diff


def make_tuple(x, y):
    z = (x, y)
    return z


def filter(volt):
    # First, design the Buterworth filter
    N = 5  # Filter order
    Wn = 0.18  # Cutoff frequency (need to optimize)
    B, A = signal.butter(N, Wn, output='ba')
    smooth_volt = signal.filtfilt(B, A, volt)  # cuts off the peak :(
    # print(type(smooth_volt))
    length = smooth_volt.size
    plt.plot(volt[0:length], 'r-')
    plt.plot(smooth_volt[0:length], 'b-')
    # plt.show()
    return(smooth_volt)


def find_peaks(x, y):
    peaks, _ = signal.find_peaks(x, height=0.2)  # does not find the last peak
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.plot(np.zeros_like(x), "--", color="gray")
    # plt.show()
    # print(peaks) # array position
    peak_voltages = x[peaks]
    # print(peak_voltages) # voltage of peaks
    beats = np.asarray(y)
    beats = beats[peaks]
    # print(peak_locations[peaks]) # time of peaks
    return(beats, peak_voltages)


def find_mean_HR(time_duration, beats):
    num_beats = beats.size
    mean_HR = num_beats/time_duration*60
    return(mean_HR)


if __name__ == "__main__":
    main()
