import re
import os
import sys
class ReadInputData:
    def __init__(self,input_file_path):
        file_path=os.path.dirname(os.path.abspath(__file__))
        input_file_path=os.path.join(file_path,'lotr.txt')
        self.input_file_path=input_file_path
        self.input_file=None
        self.file_read=0
    def read_input(self):
        try:
            #Reading as utf-8
            with open(self.input_file_path,'r',encoding='utf-8') as input_file:
                self.input_file=input_file.read()
                self.file_read=1
                print("File opened!")
        except FileNotFoundError:
            print("File not found!")
            print("Wapas check kijiye")       #If file itself is missing.
            sys.exit()
        except UnicodeDecodeError:
            print("Unicode issue..retrying with Latin method")
            try:
                with open(self.input_file_path,'r',encoding='latin-1') as input_file:
                    print("Successul open!")
                    self.input_file=input_file.read()
                    self.file_read=1
            except (EncodingWarning, UnicodeDecodeError):
                print("This open has also failed. Exiting. Fix or check the file!")
                print("Stopping execution")
                sys.exit()
        return self.input_file

    def find_length(self,input_file=None):
        if input_file is None:
            input_file=self.input_file
        elif self.file_read==0 or input_file is None:
            print("Pehle file read kar lijiye")
            sys.exit()
        #Finding total characters in the input file
        return len(input_file)
    
    def print_chars(self,input_file=None,no_of_chars=1000):   #1000 min hai. If we need more, add kar lunga
        if input_file is None:
            input_file=self.input_file
        try:
            print(input_file[:no_of_chars])
        except TypeError:
            print("File read nahi hua.\nTry reading once?")
if __name__=="__main__":      
    file1= ReadInputData('lotr.txt')
    file1.read_input()
    file1.print_chars()





        