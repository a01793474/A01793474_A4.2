""" Module to convert txt file with numbers to binary and hex"""
import sys
import os
import time
import struct
import numpy as np

def check_file(filename):
    """ Function to Validate file exists and is correct extention"""

    if os.path.exists((filename)):

        _, file_extension = os.path.splitext(filename)

        if file_extension != ".txt":
            print("File must be txt")
            return 'N'

        return 'Y'


    print("File does not exist")
    return 'N'


def get_data(path):
    """ Function to read txt file and remove non numeric characters"""
    data=[]

    with open(path, encoding='utf-8') as file:
        data=file.readlines()
        file.close()

    for i in enumerate(data):
        data[i] = data[i].replace("\n","")
        if not data[i].isdigit():
            print("Non numeric characters found and removed.")
            parce = ""
            for j in data[i]:
                if j.isdigit:
                    parce = parce+j

            if len(parce) > 0:
                data[i] = parce
            else:
                data[i] = 0


    np_data = np.array(data, dtype='float')


    return np_data

def get_bin(reg):
    """ Function to return the binary value of a float"""
    return ''.join(format(c, '08b') for c in struct.pack('!f', reg))

def get_hex(reg):
    """ Function to return the hexadecimal value of a float"""
    return hex(struct.unpack('<I', struct.pack('<f', reg))[0])

def create_file(path):
    """ Function to do Stadistical Analisis and create txt file with results """

    txtfilename = "ConvertionResults.txt"

    data = get_data(path)
    with open(txtfilename, 'a', encoding='utf-8') as f:
        f.write("FILE   NUM   REG   BIN   HEX \n")
        for i in range(0,len(data-1)):
            bin_v = get_bin(data[i])
            hex_v = get_hex(data[i])
            f.write(f"{path}   {i}   {data[i]}   {bin_v}   {hex_v} \n")
        f.write(f"Exectution Time {time.time()-init}")
        f.write("\n")
    f.close()

    print(f'Conversion file {txtfilename} created.')


file_path = sys.argv[1]

if check_file(file_path) == 'Y':

    init = time.time()
    create_file(file_path)
