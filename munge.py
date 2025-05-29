

data_open = open("data/data1.txt", "r")
information = data_open.readlines()
ofile = open("data/clean_data.csv", "w")

#To get the month in the csv
for i in information:
    if i[0] == "Y":
        headline = i
        break
array_2 = headline.split()
for j in array_2:
    j = str(j)
    j = j.strip().split()
    j = ','.join(j)
    ofile.write(j)
    ofile.write(",")
ofile.write("\n")

# To get other information in the csv format.
array_1 = []
for i in information:
    if i[0].isdigit():
        array_1 = i.split()
        for m in range(1, len(array_1)-1):
            if "*" in array_1[m]:
                continue
            else:
                array_1[m] = format((float(array_1[m])/100)*1.8,".1f")

        for j in array_1:
            j = str(j)
            j = j.strip().split()
            j = ','.join(j)
            ofile.write(j)
            ofile.write(",")
        ofile.write("\n")

data_open.close()
ofile.close()
