import csv

rows = []
with open("test.csv") as csvFile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)  # NONNUMERIC due to the file having only numbers
    for row in reader:
        rows.append(row)

column_sums = [0, 0, 0, 0]
for row in rows:
    row.append(sum(row))
    column_sums[0] += row[0]
    column_sums[1] += row[1]
    column_sums[2] += row[2]
    column_sums[3] += row[3]

print(column_sums)

with open("output.csv", 'w', newline='') as csvFileOut:  # override newline parameter as writerow also adds newline chars
    writer = csv.writer(csvFileOut, delimiter='|', quotechar=':', quoting=csv.QUOTE_ALL)
    for row in rows:
        writer.writerow(row)  # for loop can be replaced with writer.writerows(rows)
