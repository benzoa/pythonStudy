import csv
import matplotlib.pyplot as plt
from enum import Enum

IDX = Enum("IDX", "DATE LOC MEAN_TEMP MIN_TEMP MAX_TEMP", start=0)
GRAPH = Enum("GRAPH", "PLOT HIST BOXPLOT", start=0)
GRAPH_TYPE = GRAPH.PLOT.value   # GRAPH.BOXPLOT.value   # None

HIGH_TEMP_MAX_VAL = -1000
HIGH_TEMP_MAX_DATE = ''
HIGH_TEMP_MIN_VAL = 1000
HIGH_TEMP_MIN_DATE = ''

LOW_TEMP_MAX_VAL = 0
LOW_TEMP_MAX_DATE = ''
LOW_TEMP_MIN_VAL = 0
LOW_TEMP_MIN_DATE = ''
HIGH = []
LOW = []
X_SCALE = []

with open("./resource/seoul.csv", "r", encoding='cp949') as f:
    data = csv.reader(f, delimiter=",")
    header = next(data)
    print(header)

    for row in data:
        if row[IDX.MAX_TEMP.value] != '':
            row[IDX.MAX_TEMP.value] = float(row[IDX.MAX_TEMP.value])
            HIGH.append(row[IDX.MAX_TEMP.value])

            if row[IDX.MAX_TEMP.value] > HIGH_TEMP_MAX_VAL:
                HIGH_TEMP_MAX_VAL = row[IDX.MAX_TEMP.value]

            HIGH_TEMP_MAX_DATE = row[IDX.DATE.value]

            if row[IDX.MAX_TEMP.value] < HIGH_TEMP_MIN_VAL:
                HIGH_TEMP_MIN_VAL = row[IDX.MAX_TEMP.value]
                HIGH_TEMP_MIN_DATE = row[IDX.DATE.value]

        if row[IDX.MIN_TEMP.value] == '':
            continue

        row[IDX.MIN_TEMP.value] = float(row[IDX.MIN_TEMP.value])
        LOW.append(row[IDX.MIN_TEMP.value])

        if row[IDX.MIN_TEMP.value] > LOW_TEMP_MAX_VAL:
            LOW_TEMP_MAX_VAL = row[IDX.MIN_TEMP.value]
            LOW_TEMP_MAX_DATE = row[IDX.DATE.value]
        elif row[IDX.MIN_TEMP.value] < LOW_TEMP_MIN_VAL:
            LOW_TEMP_MIN_VAL = row[IDX.MIN_TEMP.value]
            LOW_TEMP_MIN_DATE = row[IDX.DATE.value]

        # print(row)
        day = row[IDX.DATE.value].split('-')[0][2:4]
        day += row[IDX.DATE.value].split('-')[1]
        day += row[IDX.DATE.value].split('-')[2]

        X_SCALE.append(int(day))

    # print(X_SCALE)
    plt.figure(figsize=(15, 3))
    plt.rc('font', family='Malgun Gothic')
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('Temperature data in Seoul from June 1, 2018 to July 31, 2020')

    if GRAPH_TYPE == GRAPH.PLOT.value:
        plt.plot(HIGH, 'red', label='HIGH')
        plt.plot(LOW, 'skyblue', label='LOW')
    elif GRAPH_TYPE == GRAPH.BOXPLOT.value:
        plt.boxplot([HIGH, LOW])
    else:
        plt.hist(HIGH, bins=800, color='red', label='HIGH')
        plt.hist(LOW, bins=800, color='skyblue', label='LOW')

    plt.legend(loc=4)
    plt.show()

    print("HIGH_TEMP")
    print(f"MAX_VAL: {HIGH_TEMP_MAX_VAL}, date : {HIGH_TEMP_MAX_DATE}")
    print(f"MIN_VAL: {HIGH_TEMP_MIN_VAL}, date : {HIGH_TEMP_MIN_DATE}")
    print("LOW_TEMP")
    print(f"MAX_VAL: {LOW_TEMP_MAX_VAL}, date : {LOW_TEMP_MAX_DATE}")
    print(f"MIN_VAL: {LOW_TEMP_MIN_VAL}, date : {LOW_TEMP_MIN_DATE}")
