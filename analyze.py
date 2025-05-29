
import csv
file = open("data/clean_data.csv")
reader = csv.reader(file)

# Using csv module.
rows = []
for row in reader:
    if "Year" in row[0]:
        continue
    if row == []:
        continue
    else:
        rows.append(row)


# Starting with the averge of each year.
sum_1 = 0
sum_array = []
years = []
for m in rows:
    sum_1 = 0
    for i in range(1,13):
        sum_1 += float(m[i]) 
    x = format((sum_1/12), ".1f")
    sum_array.append(x)
    years.append(m[0])

# Getting the group done.
answers = []
totalSum = 0
counter = 0

for temp in sum_array:
    totalSum += float(temp)
    counter += 1

    if counter == 10:
        answers.append(totalSum)
        totalSum = 0
        counter = 0

if counter > 0:
    answers.append(totalSum)

years_count = float(years[0])
for p in answers:
    print(years_count, ": ", format(float(p)/12, ".1f"), sep="")
    years_count += 10
