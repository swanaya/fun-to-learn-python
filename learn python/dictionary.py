my_dict = {
    "name": "Swanaya",
    "age": 25,
    "location": "India"
}

print(my_dict["name"])  # Output: Swanaya
print(my_dict.get("age"))  # Output: 25


my_dict["profession"] = "AI Developer"
print(my_dict)


del my_dict["age"]
print(my_dict)

for key, value in my_dict.items():
    print(f"{key}: {value}")

    def multiply(a, b):
        return a * b

# Define the function
def multiply(a, b):
    return a * b

# Example usage:
result = multiply(3, 4)
print(f"The product of 3 and 4 is {result}")