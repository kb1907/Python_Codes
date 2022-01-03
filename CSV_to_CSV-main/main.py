import csv

with open("names.csv","r") as csv_file:
    csv_data = csv.reader(csv_file)

    with open("new_names.csv", "w") as new_csv_file:
        new_csv_data= csv.writer(new_csv_file)

        for line in csv_data:
            new_csv_data.writerow(line)