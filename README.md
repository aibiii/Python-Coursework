# Python-Coursework Description

Coursework Description
General Notes
• Use user-defined functions in your solution as appropriate.
• Use descriptive names for your variables and user-defined functions.
• Reference within your code any code adapted from external or other sources.

The University requires a program to predict progression outcomes at the end of each academic
year. The program should prompt for the number of credits at pass, defer and fail
and then display the appropriate progression outcome for an individual student (i.e., progress, trailing, module retriever or exclude).

The program should display ‘Integer required’ if a credit input is the wrong data type. 
Principles I
4COSC001W: Coursework Specification Page | 3
• The program should display ‘Out of range’ if credits entered are not in the range 0, 20, 40,
60, 80, 100 and 120.
• The program should display ‘Total incorrect’ if the total of the pass, defer and fail credits is
not 120.
• A few marks will be allocated for the efficient use of conditional statements. For example,
the program does not need 28 conditional statements for 28 outcomes.

The program loops to allow a staff member to predict progression outcomes for multiple
students.
• The program should prompt for credits at pass, defer and fail and display the appropriate
progression for each individual student until the staff member enters ‘q’ to quit. Optionally
you can use an input of ‘y’ to continue.

When ‘q’ is entered, the program should produce a ‘histogram’ where each star represents a
student who achieved a progress outcome in the category range: progress, trailing, module
retriever and exclude. The histogram should relate to the data input entered during the
program run and work for any number of outcomes.
• Display the number of students for each progression category and the total number of
students.

For Part 1, most of the solutions would use variables to store the input data. For Part 2, extend your
solution so that the program saves the input progression data to a list or nested list. Then access the
stored data from the list and print the data in the following format below.

For this part you could create an additional Part 3 program or extending your original version.
Use python to save any inputted progression data to a text file.
