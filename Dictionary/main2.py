dict1=dict(name="Brundabana", age=20, city="Bangalore")
print(dict1)

student = {
    "name": "Brundabana",
    "age": 20,
    "course": "B.Tech"
}

print(student["name"])
print(student.get("age"))
print(student.keys())
print(student.values())
print(student.items())
student["course"] = "M.Tech"
print(student)