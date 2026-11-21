employee = {
    "name":"John",
    "age":34,
    "timeatwork":"2 years",
    "job":"Head of design"
}

myDictionary = {
    "apple":"a fruit",
    "computer":"a digital device",
    "water":"a drink"
}

print(employee.keys())
print(employee.values())
print(myDictionary["apple"])
print(employee["timeatwork"])

for i in employee :
    print(i,":", employee[i])

if "orange" in myDictionary :
    print("Yes")

else :
    print("No")

del (employee["timeatwork"])

for i in employee :
    print(i, ":", employee[i])

myDictionary["marks"] = [98,67,90,94,100]
print(myDictionary)
print(myDictionary["marks"][4])

userin = int(input("How old is John? "))
employee["age"] = userin
print(employee)

iusern = input("Whats the employees favourite past time?")
employee["pasttime"] = iusern

print(employee)


workers = {
    "Samuel": {
        "age":32,
        "hobby":"basketball"
    },

    "Max": {
        "age": 20,
        "hobby":"football"
    }

}

print(workers)
print(workers.keys())
print(workers.values())
print(workers["Samuel"]["hobby"])
