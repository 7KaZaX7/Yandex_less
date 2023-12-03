import csv

money = 1000
with open("wares.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    expensive = sorted(reader, key=lambda x: int(x[1]))
    buy = []
    all = [0 for i in range(len(expensive))]
    for i in expensive:
        while (all[expensive.index(i)] < 10) and (money >= int(i[1])):
            all[expensive.index(i)] += 1
            money -= int(i[1])
            buy.append(i[0])
    if buy:
        print(", ".join(buy))
    else:
        print("error")
