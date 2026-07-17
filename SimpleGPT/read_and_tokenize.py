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
        return chars
    
test_file_path='lotr.txt'
lotr_test_file=VocabbingData(test_file_path)
chars=lotr_test_file.make_set()


#Encoding karenge basic encoding for now...

character_to_integer={character : integer for integer,character in enumerate(chars)}
integer_to_character={integer: character for integer,character in enumerate(chars)}

#Now encoding and decoding

encodeded_chars= lambda a : [character_to_integer[c] for c in a]
decoded_chars= lambda b : ''.join([integer_to_character[i] for i in b])



