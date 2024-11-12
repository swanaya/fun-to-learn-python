import time

# Loop to print and write the values of i to the text file
with open("result.txt", "w", encoding="utf-8") as f: 
    for i in range(1, 100, 2):
        # Print the current value of i
        print(f"i is now {i}")
        # Write the current value of i to the file
        f.write(f"i is now {i}\n")  # \n to add a newline after each entry

# Auto brake - pause for 5 seconds before the program ends
print("Auto brake engaged. Program will exit in 5 seconds...")
time.sleep(5)  # Pause for 5 seconds before ending the program

# Optional input if you want the user to press Enter to exit
a = input()
