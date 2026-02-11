student = {
    "name": "Brundabana",
    "age": 20,
    "course": "B.Tech"
}

student.pop("age")
print(student)
del student["course"]
print(student)
student.clear()
print(student)

student["age"] = 20
print(student)
student.update({"course": "MCA"})
print(student)

student["city"] = "Gunupur"
print(student)
student.update({"college": "GIET"})
print(student)




