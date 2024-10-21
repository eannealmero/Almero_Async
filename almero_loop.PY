# input number from user
number = int(input("Enter a number for the multiplication table: "))

# counter aka number * i = the table
i = 1
# label for the table
print(f"Multiplication table for the number {number}:")
# use a while loop
while i <= 10:
    print(f"{number} x {i} = {number * i}")
# indicate that 1 is added to i until it equals to 10 (which shows the table from 1-10)
    i += 1  