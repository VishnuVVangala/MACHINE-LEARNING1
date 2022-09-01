dog = {}
print(dog)

dog = {'name': 'lucy', 'color': 'black', 'breed': 'poodle', 'legs': 4 , 'age': 3 }
print(dog)
student = dict()
student["first_name"] = "vishnu"
student["last_name"] = "reddy"
student["gender"] = "male"
student["age"] = "22"
student["martial status"] = "single"
student["skills"] = ["java", "python"]
student["country"] = "india"
student["city"] = "hyderabad"
student["address"] = "5-390"
print(student)
length = len(student)
print(length)
print(student["skills"])
print(type(student["skills"]))
student["skills"].extend(["data science"])
print(student["skills"])
print(student.keys())
print(student.values())

