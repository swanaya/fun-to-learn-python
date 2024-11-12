my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Accessing list items by index:
print(my_list[0])  # Output: 1 (indexing starts at 0)

my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5, 6]


for item in my_list:
    print(item)
    
    response = input("Press Enter to continue or type 'exit' to stop: ")
    if response.lower() == 'exit':
        break