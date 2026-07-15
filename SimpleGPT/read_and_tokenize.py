import os
from read import ReadInputData

class VocabbingData:
    def __init__(self,input_file_path):
        self.input_file_path=input_file_path
        self.reader= ReadInputData(self.input_file_path)
        self.input_file=self.reader.read_input()
    def make_set(self):
        chars=sorted(list(set(self.input_file)))
        print("Vocab size:", len(chars))
        print("Vocabulary:", ''.join(chars))
    
test_file_path='lotr.txt'
lotr_test_file=VocabbingData(test_file_path)
lotr_test_file.make_set()

