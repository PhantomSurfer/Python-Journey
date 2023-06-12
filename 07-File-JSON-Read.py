import json

student= {}

with open("sample.txt", "r") as f:
    studentString = f.read()
    student = json.loads(studentString)

print(student)
print(type(student))

f.close()