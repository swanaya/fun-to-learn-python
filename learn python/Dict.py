marks = {
    "ketivee": 90,
    "kamal": 80,
    "kamal": 85,
    0: "Ketivee",
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())  
# print(marks[0])

print("ketivee's marks are: ", marks["ketivee"] ) # prints 90, which is the value of "ketivee". It also uses a dictionary to store the values that we want to print out. This is called a dictionary comprehension. We can use this for any type of data structure in Python.
print(marks[0])
marks.update({"kamal": 100})
