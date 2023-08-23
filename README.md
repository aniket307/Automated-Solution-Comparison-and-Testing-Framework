# :zap: Automated Solution Comparison and Testing Framework
The CLI engineered an automated error detection and comparison framework to enhance software development and debugging processes. The core objective of this framework is to detect discrepancies between incorrect and correct solutions to a given problem. 

In short, suppose you write a code but it's giving wrong answer to some test case but you don't know the test case, you can use this to generate many test cases to identify on which test case it is giving wrong output.

## Components :
1. Incorrect Solution (incorrect_solution.cpp):
    This file contains the cpp code you have written which is giving wrong output to some input.
2. Correct Solution (correct_solution.cpp):
    This file contains the correct cpp code
3. Test Case Generator (test_case_generator.cpp):
    This file is used to generate random test cases which is used as input to both above file.
4. Checker Script (checker.sh): 
    This file contains the code which is used to run above files and store results of above files in seperate txt file which is used as the input and output accordingly

 ## How to run :

1. Just download all the files 
2. Open Terminal
3. Navigate to the Repository Directory
4. write command ->  bash checker.sh
5. Then just press enter and done.

## :camera: Screenshots

<p align="center">
    <img alt="Home screen" src="./screenshots/Screenshot 6.png" width="80%"/>
</p>


<p align="center">
    <img alt="Home screen" src="./screenshots/Screenshot 7.png" width="80%"/>
</p>



