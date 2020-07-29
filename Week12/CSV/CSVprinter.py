import csv
from Week12.CSV.CSVReader import CSVreader

with open('CSVIowa.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize empty dictionary
    county = {}
    for row in csv_reader:
        if all(row[0] == '' for col in row):
            continue
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        # create an item in dictionary county with a key of the county name and a value of the object
        county[str(row[0])] = CSVreader(row[1], row[2], row[3], row[4], row[5], row[6])

print(county['1'].population)

pop_sum = 0
for key in county:
    pop_sum += int(county[key].population.replace(',', ''))
print(pop_sum)

