import csv
with open("test.csv","a") as csv_file:
    csv_app = csv.writer(csv_file)
    csv_app.writerow(["New Zealand",160,30,"Auckland"])

#writing bulk rows at once
#newline='' prevents extra new line space in each row.

list = [["China",120,130,"Beijing"],["Bangladesh",30,11,"Dhaka"],["USA",23,34,"Washington"]]

with open("test1.csv","a",newline='') as csv_bulk:
    csv_app1 = csv.writer(csv_bulk)
    csv_app1.writerows(list)
