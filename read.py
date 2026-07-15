import re
import os
with open('lotr.txt','r',encoding='latin-1') as input_file:
    input_text_raw=input_file.read()

#Getting the length
print(len(input_text_raw))

print(input_text_raw[:1000])