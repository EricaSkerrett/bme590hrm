import os,sys,csv
folder = "/users/esker/MedicalDeviceSoftware/bme590hrm/test_data/" #User types in path to data folder

def main():
    files = read_files()
    open_files(files)


def read_files():
    files = []
    dirs = os.listdir( folder )
    for file in dirs:
        if file.endswith('.csv'):
            files.append(file)
    sorted(files)   #trying to put it into numerical order but it's not working
    print(files)
    return(files)


def open_files(files): #open just 1 file for now
    f=open(folder+files[0])
    csv_f = csv.reader(f)
    #print(files[0])
    time = [] #will eventually want to put these into a dictionary
    volt = []
    for i in csv_f:
        time.append(i[0])
        volt.append(i[1])
    print(time)
    print(volt)
    return(time,volt)


if __name__ == "__main__":
    main()