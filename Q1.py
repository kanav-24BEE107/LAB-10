
print("Name : Kanav ShahPatel , Roll No.: 24BEE107")
import csv

data = [
    ['Name', 'Age', 'City'],
    ['arpit', 25, 'Mehsana'],
    ['Sujal', 30, 'Surat'],
    ['Aniket', 35, 'Delhi']
]
with open('kanav.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print("Done")
