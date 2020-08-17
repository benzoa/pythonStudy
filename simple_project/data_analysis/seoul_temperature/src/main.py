import csv
import matplotlib.pyplot as plt
from enum import Enum

Idx = Enum("Idx", "DATE LOC MEAN_TEMP MIN_TEMP MAX_TEMP", start=0)
high_temp_max_val = -1000
high_temp_max_date = ''
high_temp_min_val = 1000
high_temp_min_date = ''

low_temp_max_val = 0
low_temp_max_date = ''
low_temp_min_val = 0
low_temp_min_date = ''
high = []
low = []

with open("./resource/seoul.csv", "r", encoding='cp949') as f:
    data = csv.reader(f, delimiter=",")
    header = next(data)
    print(header)

    for row in data:
        if row[Idx.MAX_TEMP.value] != '':
            row[Idx.MAX_TEMP.value] = float(row[Idx.MAX_TEMP.value])
            high.append(row[Idx.MAX_TEMP.value])
        
            if row[Idx.MAX_TEMP.value] > high_temp_max_val:
                high_temp_max_val = row[Idx.MAX_TEMP.value]
                high_temp_max_date = row[Idx.DATE.value]
            
            if row[Idx.MAX_TEMP.value] < high_temp_min_val:
                high_temp_min_val = row[Idx.MAX_TEMP.value]
                high_temp_min_date = row[Idx.DATE.value]
        
        if row[Idx.MIN_TEMP.value] == '':
            continue
        
        row[Idx.MIN_TEMP.value] = float(row[Idx.MIN_TEMP.value])
        low.append(row[Idx.MIN_TEMP.value])

        if row[Idx.MIN_TEMP.value] > low_temp_max_val:
            low_temp_max_val = row[Idx.MIN_TEMP.value]
            low_temp_max_date = row[Idx.DATE.value]
        elif row[Idx.MIN_TEMP.value] < low_temp_min_val:
            low_temp_min_val = row[Idx.MIN_TEMP.value]
            low_temp_min_date = row[Idx.DATE.value]

        # print(row)
    

    plt.figure(figsize = (15, 3))
    plt.rc('font', family = 'Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('Temperature data in Seoul from June 1, 2018 to July 31, 2020')
    plt.plot(high, 'red')
    plt.plot(low, 'skyblue')
    plt.show()
    print(f"high_temp_max_val : {high_temp_max_val}, date : {high_temp_max_date}")
    print(f"high_temp_min_val : {high_temp_min_val}, date : {high_temp_min_date}")
    print(f"low_temp_max_val : {low_temp_max_val}, date : {low_temp_max_date}")
    print(f"low_temp_min_val : {low_temp_min_val}, date : {low_temp_min_date}")
