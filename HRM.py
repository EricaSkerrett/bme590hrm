import os
import sys
import csv
import scipy
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import json

folder = "/users/esker/MedicalDeviceSoftware/bme590hrm/test_data/"


def show_dir(folder):
    """Extracts files in the specified directory.

    Args:
        param1 (str): path to folder with files to be collected

    Returns:
        List of directories

    """
    if not isinstance(folder, str):
        raise TypeError("Path to folder with test data must "
                        "be entered as string")
    dir = os.listdir(folder)
    return(dir)


def read_files(dir):
    """Prints only .csv files from directory into list

    Args:
        param1 (list): list of directories

    Returns:
        List of .csv files from directory

    """
    files = []
    for file in dir:
        if file.endswith('.csv'):
            files.append(file)
    if dir == []:
        raise IndexError("No .csv files present in folder")
    return(files)


def open_files(files):  # open just 1 file for now
    """Prints names of only .csv files from directory into list

    Args:
        param1 (list): path to folder with files to be collected

    Returns:
        Reader object with lines from .csv file

    """
    f = open(folder + files[0])
    csv_f = csv.reader(f)
    return(csv_f)


def split_into_array(csv_f):
    """Splits up arrays of time and voltage data

    Args:
        param1 (object): reader object with lines from .csv file

    Returns:
        2 lists of floats for times and voltages from .csv file

    """
    time = []  # will eventually want to put these into a dictionary
    volt = []
    # rawdata = []
    for i in csv_f:
        time.append((i[0]))
        volt.append(float(i[1]))
        # rawdata.append([i[0], i[1]])
    volt = [float(i) for i in volt]
    time = [float(i) for i in time]
    return(time, volt)


def extremes(x):
    """Find extremes of a list of floats

    Args:
        param1 (lst): list of floats

    Returns:
        2 floats - max and min values of the list

    """
    max_x1 = max(x)
    min_x1 = min(x)
    max_x = float(max_x1)
    min_x = float(min_x1)
    return(max_x, min_x)


def find_duration(x, y):
    """Finds difference between 2 numbers

    Args:
        param1 (float)
        param2 (float)

    Returns:
        float - difference between 2 values

    """
    diff = x - y
    return diff


def make_tuple(x, y):
    """Converts 2 floats into a tuple

    Args:
        param1 (float)
        param2 (float)

    Returns:
        Tuple of 2 values

    """
    z = (x, y)
    return z


def filter(volt):
    """Send noisy signal through butterworth filter

    Args:
        param1 (lst): List of floats

    Returns:
        Array

    """
    N = 5  # Filter order
    Wn = 0.18  # Cutoff frequency (need to optimize)
    B, A = signal.butter(N, Wn, output='ba')
    smooth_volt = signal.filtfilt(B, A, volt)
    length = smooth_volt.size
    plt.plot(volt[0:length], 'r-')
    plt.plot(smooth_volt[0:length], 'b-')
    plt.show()
    return(smooth_volt)


def find_peaks(x, y):
    """Use thresholds to find peaks

    Args:
        param1 (array): Array for peak detection
        param2 (list): list of times

    Returns:
        Array of peak values and array of times of peaks

    """
    peaks, _ = signal.find_peaks(x, height=0.2)  # does not find the last peak
    plt.plot(x)
    plt.plot(peaks, x[peaks], "x")
    plt.plot(np.zeros_like(x), "--", color="gray")
    plt.show()
    peak_voltages = x[peaks]
    beats = np.asarray(y)
    beats = beats[peaks]
    # print(beats)
    # print(peak_voltages)
    return(beats, peak_voltages)


def get_input(time_duration):
    time_avg = time_duration
    user_avg = input("Type time for mean heart rate:  ")
    type(user_avg)
    user_avg = int(user_avg)
    if user_avg < time_duration:
        time_avg = user_avg
    return time_avg


def find_mean_HR(time_duration, beats):
    """Finds mean over entire duration of signal

    Args:
        param1 (float): time duration
        param2 (array): array of beat times

    Returns:
        (float) mean heart rate

    """
    num_beats = beats.size
    mean_HR = num_beats/time_duration*60
    return(mean_HR, num_beats)


def make_dict(files, mean_hr_bpm, voltage_extremes, time_duration,
              num_beats, beats):
    """Inserts all parameters into dictionary called metrics

    Args:
        param1 (list): files
        param2 (int): mean hr (bpm)
        param3 (tuple): voltage extremes
        param4 (float): time duration
        param5 (int): number of beats
        param6 (array): array of beat times

    Returns:
        (dict) compiled metrics

    """
    beats = beats.tolist()  # so that dictionary can be stored as JSON
    metrics = dict([
        ('File_Name', files[0]),  # Only the first file for now
        ('Mean_HR_(BPM)', mean_hr_bpm),
        ('Voltage_Extremes', voltage_extremes),
        ('Data_Duration', time_duration),
        ('Number_Beats', num_beats),
        ('Time_of_Beats', beats),
    ])
    return(metrics)


def make_json(dictionary, files):
    """Outputs dictionary as a JSON file

    Args:
        param1 (dict): dictionary storing metrics
        param2 (lst): list of file names

    Returns:
         JSON file in project folder

    """
    file_name = str(files[0])
    with open(file_name, 'w') as fp:
        json.dump(dictionary, fp)  # come back to fix how the data is stored


if __name__ == "__main__":
    dir = show_dir(folder)
    files = read_files(dir)
    csv_f = open_files(files)
    (time, volt) = split_into_array(csv_f)
    (max_t, min_t) = extremes(time)
    (max_v, min_v) = extremes(volt)
    time_duration = find_duration(max_t, min_t)  # Time duration of ECG strip
    voltage_extremes = make_tuple(max_v, min_v)  # Tuple of min/max voltages
    smooth_volt = filter(volt)
    (beats, peak_voltages) = find_peaks(smooth_volt, time)  # np arrays of
    time_avg = get_input(time_duration)
    (mean_hr_bpm, num_beats) = find_mean_HR(time_avg,
                                            beats)
    metrics = make_dict(files, mean_hr_bpm, voltage_extremes, time_duration,
                        num_beats, beats)
    make_json(metrics, files)
