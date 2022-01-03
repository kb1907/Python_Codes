import csv
html_output = ""
names = []

with open("Name.csv") as name_file:
    names_data= csv.reader(name_file)

    """Don't want to add two lines of bad data"""
    next(names_data)
    next(names_data)

    for line in names_data:
        names.append(f"{line[0]} {line[1]}\t\t{line[2]}")

html_output += f"<p> There are currently {len(names)} people in the list.</p>"

html_output += "\n<ul>"

for name in names:
    html_output += f"\n\t<li> {name}</li>"

html_output += "\n</ul>"

file = open("name.html", "w")
file.write(html_output)
file.close()






