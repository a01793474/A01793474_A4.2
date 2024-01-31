""" Module to count words in a txt file """
import sys
import os
import time
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

    with open(path,encoding='utf-8') as file:
        data=file.readlines()
        file.close()

    for i in enumerate(data):
        data[i] = data[i].replace("\n","")

    np_data = np.array(data)
    return np_data

def create_file(path):
    """ Function to do Stadistical Analisis and create txt file with results """
    txtfilename = "WordCountResults.txt"

    data = get_data(path)

    unique, counts = np.unique(data, return_counts=True)
    data_count = dict(zip(unique, counts))
    data_count = dict(sorted(data_count.items(), key=lambda x: x[1], reverse=True))
    data_li = list(data_count.keys())

    with open(txtfilename, 'a', encoding='utf-8') as f:
        f.write("FILE   NUM   WORD   COUNT \n")
        num=1
        for i in data_li:
            f.write(f"{path}   {num}   {i}   {data_count[i]} \n")
            num=num+1
        f.write(f"Exectution Time {time.time()-init}")
        f.write("\n")
    f.close()

    print(f'Conversion file {txtfilename} created.')

file_path = sys.argv[1]

if check_file(file_path) == 'Y':

    init = time.time()
    create_file(file_path)
