# import sys
from sys import argv
import random


# This assignment is called Better Know a Chicago Landmark.
# We'll develop a tool to encourage you to go out and see beautiful
# Chicago landmarks.  The dataset is from the Chicago Open Data Portal at:
# https://data.cityofchicago.org/

# We'll do this by reading in a dataset, then randomly choosing a line from it
# to read back out to the user.

# Note that the steps in this assignment are numbered but not in order in
# this file.  Work in order of the numbers.  Each number's position is intended
# to help you put your code in the right places.

# 2.  Write a function that takes a file path and returns an open file
#     object.  Call this function immediately after parsing your commandline
#     arguments in step (1).

def open_file(my_file):
    text=open(my_file)
    return text
    # text=open(my_file)
    # return text.read()


# 4.  Write a function that takes an int called n_chars and returns a random
#     integer between 0 and n_chars, inclusive.
#     Hint:  call a function from the random module

def random_int(low,n_chars):
    return random.randint(0,FILE_SIZE_CHARS)





# 8.  Write a function that takes a string and prints it out, with the
#    following text prepended.
#    'Why not go visit this beautiful Chicago Landmark?'

def recommendation(line):
    print 'Why not go visit this beautiful Chicago Landmark?'
    print line



#    This function takes a file object and an integer.
#    The integer represents a character position in the file.
#    It reads and returns the rest of the line that character is on.
def seek_and_readline(my_file, curs):
    my_file.seek(curs)
    return my_file.readline()



# 1. Read the path to the dataset in from a commandline arguement.
#    i.e. your program should run if you enter:
#       python landmark_starter.py Individual_Landmarks.csv
#    from the commandline

script, my_file = argv

opened_file_object= open_file(my_file)




# 3.  Now  compute how many characters are in this
#     file and assign that value to a variable called FILE_SIZE_CHARS.
#     Hint:  You'll need to read the file.
#     Hint:  the builtin len() function gives the number of charachters
#     in a str.  Example:  len('my string') is 9.

read_file=opened_file_object.read()
# print read_file
FILE_SIZE_CHARS= len(read_file)
# print FILE_SIZE_CHARS
# print random.randint(0,FILE_SIZE_CHARS)



# 5.  Now write a line  that passes the value from step (3) to
#     the function you wrote in (4).  Save the resulting value to
#     a variable.

curs= random_int(0,FILE_SIZE_CHARS)
# curs=1
# print curs



# 6.  Call the seek_and_readline function above with your file object and the
#     value you computed in (5).  Note that that value represents a randomly
#     selected curson position you're going to go to in the file.  For now,
#     print the value out.
#
printed_line= seek_and_readline(opened_file_object,curs)
# print printed_line

 # def seek_and_readline(my_file, curs):
#     my_file.seek(curs)
#     return my_file.readline()

# 7.  Note that the line we printed in (6) is (probably) inpcomplete.  Let's
#     print the next whole line.  In case we run off the end of the file,
#     we'll wrap around to the beginning.  All you have to do here is
#     uncomment these lines.
if opened_file_object.tell() >= FILE_SIZE_CHARS:
    opened_file_object.seek(0)

next_line=opened_file_object.tell()
# print next_line
# print seek_and_readline(opened_file_object,next_line)




# 9.  Change the last line above to call the function you wrote in Step (8)
#     instead.

recommendation(seek_and_readline(opened_file_object,next_line))




# 10.  Change your program to produce 3 suggestions instead of just 1
#      by putting some of your code into a function and calling it 3 times.

next_line=opened_file_object.tell()
# print next_line
recommendation(seek_and_readline(opened_file_object,next_line))
next_line=opened_file_object.tell()

recommendation(seek_and_readline(opened_file_object,next_line))

# 11. In your own words, explain what the tell() function is doing.
# The tell() function is showing the position of the cursor in the file as an integer.
