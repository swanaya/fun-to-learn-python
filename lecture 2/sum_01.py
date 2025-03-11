n = 5
sum = 0  # Initialize sum

for i in range(1, n + 1):
    print(i)
    sum += i

print(sum)  # This will now work correctly.

num = 10
sum = 0  # Re-initialize sum

for i in range(1, num + 1):
    sum += i
    print(sum)