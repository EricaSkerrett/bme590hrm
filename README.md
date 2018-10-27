#bme590hrm
##ECG Monitor Assignment

Note: Readme.md will be updated Sunday evening

___

*Code Pupose*

- The code reads all ".csv" files in the folder specified by the user. The user must enter the path to the folder
containing the documents they want analyzed into HRM.py next to `folder = `. The path must be entered as a string.

-The python code can be run after installing the requirements listed in requirements.txt. Currently, no inputs are
needed, but my goal is to have the user type in the minutes that they want the average heart rate averaged over. 

- The code runs through the ".csv" files and sorts them in alphabetical and numerical order. It currently only reads
the first file, simply as a way for me to minimize the complexity and finish the other tasks. 

- From that file, the code will output a JSON file containing the mean heart rate over the entire duration, the minimum
and maximum voltages, the duration of the data, the total number of beats, and the times when those beats occurred.

____

*Friday Night Update/ Weekend Fun*

I had a late start and still have *many* things to do for Sunday, including:

- General coding goals

    - Confirm functionality of the threshold detection dictionary
    
    - Use threshold detection array length to get # beats and their times
    
    - Will use the max time of the input data to calculate the average BPM
    
        - This will be overridden if the user inputs a value less than the maz length of the array
        - A reach goal is to have the user be able to input that number when they type in the name of the python file
        in their terminal
    
    - Store metrics into dictionary and output as JSON
        
        - The dictionary will be exported into JSON with json.dump
        
   
- Things to focus on 

    - I'm running into issues with the exceptions and logs and tying those into the unit tests. Anything beyond the 
    simple assert statements for the unit test is taking a while, but it's obviously an important part of the code, so I 
    hope to have that figured out by Sunday night.
    
    - Docstrings! 
    

