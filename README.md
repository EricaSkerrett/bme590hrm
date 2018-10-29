#bme590hrm

##ECG Monitor Assignment

Note: Readme.md will be updated Sunday evening

___

*Code Pupose*

- The code reads all ".csv" files in the folder specified by the user. The user must enter the path to the folder
containing the documents they want analyzed into HRM.py next to `folder = `. The path must be entered as a string.

- The python code can be run after installing the requirements listed in requirements.txt. User types `python HRM.py` to
run the program. During the program, a couple graphs will appear showing the filtering and peak detection steps for the
user to monitor the progress. 

    - Afterwards, the user will be prompted to type in the time that they wish to have the heart rate averaged over (in
    minutes). If this time is longer than the length of the dataset, the program will default to use the length of the 
    dataset.

- The code runs through the ".csv" files from the specified directory. It currently only reads
the first file, simply as a way for me to minimize the complexity and finish the other tasks. 

- From that file, the code will outputs a JSON file containing the mean heart rate over the entire duration, the minimum
and maximum voltages, the duration of the data, the total number of beats, and the times when those beats occurred.

____

*Issues with Code*

- Docstrings not properly output to Sphinx
- Very spotting unit testing, partly due to trouble unit testing the exceptions (When I tested for exceptions, I 
was unable to pass pytest)
- Only reads 1 file
