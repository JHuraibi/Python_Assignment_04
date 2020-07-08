# Author: Jamal Huraibi, fh1328
# Assignment 4
# Question 1
# Note: Referenced datetime information from docs.python.org
#                now():     https://docs.python.org/3/library/datetime.html#datetime.datetime.now
#           strftime():     https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

import datetime


# TODO: Determine how to reference file data
# e.g. Load/Read file each time or keep local copy in a str var?
# TODO: Change self.file_ref to a method-only scope?
class File:
    def __init__(self, initial_file_name, initial_content=" "):
        self.file_number = None
        self.file_name = None
        self.file_owner = " "
        self.time_modified = None
        self.content = initial_content
        self.date_last_modified = " "
        
        self.__initial_setup(initial_file_name)
        
        self.file_ref = None    # TODO: Update to match future method of handling file opening

    
    def __initial_setup(self, initial_file_name):
        self.__generate_file_name(initial_file_name)                            # Set/generate and set file name
        self.__create_file()
        self.__update_file_counter()
        self.__update_date_modified()                                           # Update the time last modified
        
    # TODO: Name is not being set correctly
    def __generate_file_name(self, name):
        """Checks if a file already exists with the intended file-name.
        If no: returns the available file name.
        If yes: Concatenate a modifier to the file name, re-check with the modified name.
        Value of variable "name" is never altered.
        """
        import os
        modifier = 1
        possible_name = str(name) + str(modifier) + ".txt"
    
        while os.path.exists(possible_name):
            print("File with name [{}] exists.".format(possible_name))
            modifier = float(modifier) + 1
            possible_name = str(name) + str(modifier) + ".txt"
        
        self.file_name = possible_name
    
    
    def __create_file(self):
        """Creates a file with the name set by __generate_file_name"""
        file = open(self.file_name, "x")
        print("File created with name [{}].".format(self.file_name))
        
    
    @staticmethod
    def __update_file_counter():
        """Updates the file-number counter."""
        pass
    
    
    def get_number(self):
        """Returns the file number."""
        return self.file_number
        
        
    def get_name(self):
        """Returns the file name."""
        return self.file_name
    
    
    def set_owner(self, owner_name):
        """Updates the name of the file owner."""
        self.file_owner = owner_name
        self.__update_date_modified()                                           # Update the time last modified
        
        
    def get_owner(self):
        """Returns the name of the file owner (if one was set). Otherwise, returns an alert that none was set."""
        if self.file_owner == " ":
            return "[No Owner Has Been Set]"                                    # Handle file having no owner
        else:
            return self.file_owner                                              # If has owner, return the name
        
        
    def __update_date_modified(self):
        """Updates the last date and time file was modified (i.e. time when method was called)."""
        self.date_last_modified = datetime.datetime.now()
        
        
    def get_date(self):
        """Returns the last date and time file was modified."""
        return self.date_last_modified
    
    # TODO: Instructions don't give a date format to use
    def print_date_style_1(self):
        """Prints date-modified as HH:MM:SS on MM/DD/YYYY"""
        date_ref = self.get_date()                                              # Establish a reference to the datetime
        time = date_ref.strftime("%X")                                          # HH:MM:SS
        date = date_ref.strftime("%x")                                          # MM/DD/YYYY
        
        print("Date Last Modified: {} on {}".format(time, date))                # Print date as "HH:MM:SS on MM/DD/YYYY"
        
        
    def add_line(self, text_to_add):
        """Adds a new line to the end of file."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        
        self.file_ref.write(text_to_add)                                        # Append the new data
        
        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
        
    
    def delete_line(self, line_number):
        """Deletes a specific line from file."""
        
        # Textbook states 'rw' is a mode (p.122). Typo?
        self.file_ref = open(self.file_name, 'r+')                              # Open the file in read/write mode
        
        content = self.file_ref.read()                                          # Store file contents as single string
        content_by_lines = content.split('\n')                                  # Delimit by new line
        num_of_lines = len(content_by_lines)                                    # Record how many lines there are
        
        if line_number < 1:
            print("Line number must be 1 or greater")                           # Invalid line number entered
            return None
        elif (line_number - 1) > num_of_lines:
            print("There are only {} lines".format(num_of_lines))               # Line to erase doesn't exist
            return None
        
        removed_line = content_by_lines.pop(line_number - 1)                    # Remove content at intended line number
        print("Removing line {}".format(line_number))                           # Confirmation of line removed
        print("Content that was removed: {}".format(removed_line))              # Confirmation of what was removed
        
        rebuilt_content = "".join(content_by_lines)                             # Convert List back into single string
        self.file_ref.write(rebuilt_content)                                    # Write the updated content to file
        
        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
        
    # TODO: Clarify if printing or just return raw content
    def get_content(self):
        """Fetches the entire content of the file and returns it."""
        self.file_ref = open(self.file_name, 'r')                               # Open the file in read mode
        all_content = self.file_ref.read()                                      # Read-in data as single string
        
        self.file_ref.close()                                                   # Close the file
        
        return all_content                                                      # Return the content
        
        
    def set_content(self, new_content):
        """Changes the content of the text file, overwriting any existing text."""
        self.file_ref = open(self.file_name, 'w')                               # Open the file in read/write mode
        self.file_ref.write(new_content)                                        # Write the new content
        self.file_ref.close()                                                   # Close the file
        
        self.__update_date_modified()                                           # Update the time last modified
        
        
    def has_word(self, word_to_find):
        """Checks if the file has a specific word in it. Returns true if the word is found, otherwise returns false."""
        return word_to_find in self.content
    
    # TODO: Add error handling
    def __update_local_content(self):
        self.file = open(self.file_name, 'r')                                   # Open the file in read mode
        self.content = self.file.read()                                         # Store file contents as single string
        self.file.close()                                                       # Close the file
    
    # TODO: Make sure other file content is str (check: .write() cannot do numbers, p. 119)
    def add_from(self, other_file):
        """Adds the content of the other file to the end of the current file."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        other_file_content = other_file.get_content()                           # Load the contents of the other file
        
        self.file_ref.write(other_file_content)                                 # Append the data from the other file
        
        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
    
    # TODO: Make sure unwanted items are not being counted
    def count_words(self):
        """Counts the number of words in a file and returns it."""
        self.file_ref = open(self.file_name, 'a')                               # Open the file in append mode
        raw_content = self.file_ref.read()                                      # Store content as single string
        words = raw_content.split()                                             # Separate into individual words

        self.file_ref.close()                                                   # Close the file
        
        return len(words)                                                       # List length == num of indiv. words
    
    
    def replace(self, target, replacement):
        """Replaces (target: str) with (replacement: str) everywhere in the file."""
        self.file_ref = open(self.file_name, 'r+')                              # Open the file in read/write mode
        raw_content = self.file_ref.read()                                      # Store content as single string
        
        updated_content = raw_content.replace(target, replacement)              # Replace occurrences of target substr.
        
        self.file_ref.write(updated_content)                                    # Write updated content to file

        self.file_ref.close()                                                   # Close the file
        self.__update_date_modified()                                           # Update the time last modified
    
    
    def open_file(self):
        self.file_ref = open(self.file_name, 'r')                               # Open the file in read mode
        # Don't close yet, the calling method will access the file
        # !! Critical: Ensure calling method closes file


if __name__ == '__main__':
    # A = File("test")
    # B = File("test")
    # C = File("test")
    #
    # print("A File Number: {}".format(A.get_number()))
    # print("B File Number: {}".format(B.get_number()))
    # print("C File Number: {}".format(C.get_number()))
    #
    # print("C File Date: {}".format(C.get_date()))
    # C.print_date_style_1()
    
    A = File("test1", "This is a file with some text")
    B = File("test2")
    C = File("test1", "This is another file with some text")
    D = File("test2")
    
    C.set_owner("John Doe")
    D.set_owner("Runtao Zhu")
    
    print(A.get_owner())
    print(D.get_owner())
    
    D.set_content("This is a new content")
    D.add_from(A)
    D.get_date()
    B.add_line("Hello World!")
    B.add_line("This is a new line!")
    B.delete_line(1)
    print(A)
    
    # replaces the word "this" with the word "that" everywhere in the file.
    A.replace("this", "that")
    
    print(A.get_content())

    # returns true if the file contains the word this
    B.has_word("World")

    # TODO: Overriding methods
    # The content of A and B are added together and written into a new file E.
    # E = A + B
    # print("A + B = {}".format(E))

    # returns true, if the number of words in A is greater than the number of words in B
    # print("A > B is {}".format(A > B))