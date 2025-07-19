# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to draw each row
while row < size:
    # Use a for loop to draw asterisks in the current row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
