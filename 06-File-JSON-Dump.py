import json

student = {
    "name": "Felix",
    "course": "BS Computer Science",
    "student_number": 1,
    "isAbsent": False
}

studentString = json.dumps(student, indent = 4)
print(studentString)

with open("sample.txt", "w") as f:
    f.write(studentString)

f.close()
# with open("sample.txt", "r") as f:
#     file_contents = f.read()
#     print(file_contents)