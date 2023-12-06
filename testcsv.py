import csv
file = open('robotstxt2.csv')
csvreader = csv.reader(file)

for row in csvreader:
    print(row)
