""" Module to read txt file with numbers and generate txt file with statistical analisis"""

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

    file = open(path,encoding='utf-8')
    data=file.readlines()
    file.close()

    for i,_ in enumerate(data):
        data[i] = data[i].replace("\n","")
        if not data[i].isdigit():
            print("Non numeric characters found and removed.")
            parce = ""
            for j in data[i]:
                if j.isdigit():
                    parce = parce+j

            if len(parce) > 0:
                data[i] = parce
            else:
                data[i] = 0

    np_data = np.array(data, dtype='float')


    return np_data


def get_mean(data):

    """ Function to Calculate de Mean """ 
    x=0

    for i in data:
        x =x+i

    return x/len(data)


def get_median(data):

    """ Function to Calculate de Median """

    data_order = np.sort(data)
    y = len(data_order)/2

    if (y % 2) != 0:
        a = round(y)
        cal_med = (data_order[a-1]+data_order[a])/2
    else:
        cal_med = data_order[int(y)]

    med = cal_med

    return med


def get_mode(data):

    """ Function to Calculate de Mode """

    unique, counts = np.unique(data, return_counts=True)
    count = dict(zip(unique, counts))
    sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return sort_count[0][0]


def get_var(data, mean):

    """ Function to Calculate de Variance """

    x = 0
    s = 0
    for i in data:
        x = pow(i-mean, 2)
        s = s+x
    var = s/len(data)

    return var


def create_file(path):

    """ Function to do Stadistical Analisis and create txt file with results """

    txtfilename = "StatisticsResults.txt"

    data = get_data(path)
    mean = get_mean(data)
    median = get_median(data)
    mode = get_mode(data)
    var = get_var(data, mean)
    sdev = np.sqrt(var)

    with open(txtfilename, 'a', encoding='utf-8') as f:
        f.write(f"Stadistics for {path}\n")
        f.write(f"Count = {len(data)}\n")
        f.write(f"Mode = {mode}\n")
        f.write(f"Mean = {mean}\n")
        f.write(f"Median = {median}\n")
        f.write(f"Standard Deviation = {sdev}\n")
        f.write(f"Variance = {var}\n")
        f.write(f"Execution time = {time.time()-init}\n")
        f.write("\n")
        f.close()

    print(f'Stadistics file {txtfilename} created.')


file_path = sys.argv[1]

if check_file(file_path) == 'Y':

    init = time.time()
    create_file(file_path)
