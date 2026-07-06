import csv

students = []

with open("row.csv", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for name, friend in reader:
        if name and friend:
            students.append({"name": name, "friend": friend})

for student in sorted(students, key=lambda student: student["friend"]):
    print(f"{student['name']} is in {student['friend']}")

        


