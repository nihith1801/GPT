import os
from read import ReadInputData
import torch
import sys
class TestVocabbingData:
    def __init__(self,input_file_path):
        self.input_file_path=input_file_path
        self.reader= ReadInputData(self.input_file_path)
        self.input_file=self.reader.read_input()
    def make_set(self):
        chars=sorted(list(set(self.input_file)))
        print("Vocab size:", len(chars))
        print("Vocabulary:", ''.join(chars))
        return chars
    def make_string(self):
        character_string=str(self.input_file)
        return character_string

#Encoding karenge basic encoding for now...


#Now encoding

class SampleEncoderAndDecoder:
    def __init__(self,text):
        self.text=text
        self.string_to_integer={character : integer for integer,character in enumerate(text)}
        self.integer_to_string={integer: character for integer,character in enumerate(text)}
        self.encoder= lambda a : [self.string_to_integer[c] for c in a]
        self.decoder= lambda b : ''.join([self.integer_to_string[i] for i in b])
    def encode(self):
        encoded_data=torch.tensor(self.encoder(self.text),dtype=torch.long)
        return encoded_data
    def decode(self):
        pass



class TrainAndValidation (SampleEncoderAndDecoder):
    def __init__(self, text, split_percentage):
        super().__init__(text)
        self.split_percentage=split_percentage   #Setitng the split percentage

    def train_validation_split(self):
        if self.split_percentage==0.0 or self.split_percentage==1.0:
            print(f"Split kya hi karoge? Choose a better split. Current split: {self.split_percentage}\n Closing the program ")     #Split karenge abhi
            sys.exit()
        split=int(self.split_percentage*len(self.text))
        train_data=self.text[:split]
        test_data=self.text[split:]
        return train_data, test_data



        




    
if __name__=="__main__":
    test_file_path='lotr.txt'
    test_file=TestVocabbingData(test_file_path)
    chars=test_file.make_string()
    encoded_chars=SampleEncoderAndDecoder(chars)
    data=encoded_chars.encode()
    print(data[:50])
