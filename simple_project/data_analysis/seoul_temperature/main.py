import csv

max_temp = -1000
max_date = ''

with open("./seoul.csv", "r", encoding='cp949') as f:
    data = csv.reader(f, delimiter=",")
    header = next(data)
    print(header)

    for row in data:
        # if data is missing, enter 1000
        if row[-1] == '':
            row[-1] = 1000
        
        row[-1] = float(row[-1])

        if row[-1] != 1000 and row[-1] > max_temp:
            max_temp = row[-1]
            max_date = row[0]
        
        print(row)

    print(f"max_temp : {max_temp}, max_date : {max_date}")
