import os
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''This script will modify all the files in the current directory.
It works recursively on all subdirectories.
It will insert the input string on a required place as mentioned with respect to
some text.
There are two user inputs, first is the text after which to append and
second is the text to append''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
replace_text = input("Enter the text after which you want to append : ")
insert_text = input("Enter the text to append: ")

''''''''''''''''''''''''''''''''''''''''''''
'''Required Modules'''
''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Reads the input file, and returns a list of the lines in file.
Each line is a string.''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def read_file(input_file):
    try:
        inputFile = open(input_file, 'r')  # opening the input_file for reading.
        return inputFile.readlines()
    except:
        # if any file not exist or fails to open, The program will not stop.
        print ("There was some problem with file "+input_file+".")

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Writes the input lines in the out_file.
The out_file is the one that was read earlier in read_file().''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def write_file(out_file, lines):
    with open(out_file, 'w') as outFile:
        for line in lines:
            outFile.write(line)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''Modifies a line by placing some text on a location after some text.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def modify_line(line, replace_text, text):
    new_line = line
    location = line.find(replace_text)
    if location != -1:  # text found
        # new_line, assigned the old line with insertion of the text.
        new_line = line[:location]+text+line[location+len(replace_text):]
    # returning the new_line with the location after, text was found.
    return new_line


'''''''''''''''''
The main module
'''''''''''''''''


def main(dir_, replace_text, insert_text):
    for each_file in os.listdir(dir_+"/"):  # for each file in input dir_.
        # if the file is not a directory.
        if not os.path.isdir(dir_+"/"+each_file):

            if not each_file.endswith('.py') and not each_file.endswith(
                    '.pyc'):  # so as to not enter the script itself.
                print (each_file)
                lines_in_file = read_file(dir_+"/"+each_file)  # reading file
                lines_to_write = []  # list to write new lines

                for line in lines_in_file:  # iterating over the lines_in_file.
                    line = modify_line(line, replace_text, insert_text)
                    lines_to_write.append(line)  # appending the line to list

                # writing the new lines to file.
                write_file(dir_+"/"+each_file, lines_to_write)
        else:
            # Go through the subdirectory.
            main(dir_+"/"+each_file, replace_text, insert_text)

if __name__ == main(r'.', replace_text, insert_text):
    # calling the main() with current directory
    main(r'.', replace_text, insert_text)