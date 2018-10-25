import os
import sys
import csv
import scipy
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

folder = "/users/esker/MedicalDeviceSoftware/bme590hrm/test_data/"
# User types in path to data folder


def main():
    files = read_files()
    (time, volt, rawdata) = open_files(files)
    print(volt)
    (max_t, min_t) = extremes(time)
    (max_v, min_v) = extremes(volt)
    # extremes(volt)
    smooth_volt = filter(volt)


def read_files():
    files = []
    dirs = os.listdir(folder)
    for file in dirs:
        if file.endswith('.csv'):
            files.append(file)
    sorted(files)  # trying to put it into numerical order but it's not working
    # print(files)
    return(files)


def open_files(files):  # open just 1 file for now
    f = open(folder + files[0])
    csv_f = csv.reader(f)
    # print(files[0])
    time = []  # will eventually want to put these into a dictionary
    volt = []
    rawdata = []
    for i in csv_f:
        time.append(i[0])
        volt.append(float(i[1]))
        rawdata.append([i[0], i[1]])
    # print(time)
    # print(volt)
    return(time, volt, rawdata)


def extremes(x):
    max_x = max(x)
    min_x = min(x)
    # print(max_x)
    # print(min_x)
    return(max_x, min_x)


def filter(volt):
    # First, design the Buterworth filter
    N = 5  # Filter order
    Wn = 0.18  # Cutoff frequency (need to optimize)
    B, A = signal.butter(N, Wn, output='ba')
    smooth_volt = signal.filtfilt(B, A, volt)  # cuts off the peak :(
    plt.plot(volt[0:500], 'r-')
    plt.plot(smooth_volt[0:500], 'b-')
    plt.show()
    return(smooth_volt)


if __name__ == "__main__":
    main()
