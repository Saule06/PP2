import json

with open("students.json", "r") as file:
    data = json.load(file)
with open("intructurs.json", "r") as file:
    data1 = json.load(file)

print("INSTRUCTOR          STUDENTS")
print("-" * 35)
for instructor in data1["instructurs"]:
    print(instructor["name"])
    for student in data["Students"]:
        if student["course"] == instructor["course"]:
            print(f"                   {student['name']} {student['course']}")
    print()