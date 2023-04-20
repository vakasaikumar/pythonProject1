"""sum = 0  # initialize sum to zero

response = input("Enter 'yes' to start  numbers, 'no' to exit: ")
while response.lower() == "yes":
    num = int(input("Enter a number: "))
    sum += num
    response = input("Enter 'yes' to continue entering numbers, 'no' to exit: ")

if response.lower() == "no":
    print("Sum of all numbers entered:", sum)
else:
    print("Invalid input. Please enter either 'yes' or 'no'.")

total_sum = 0  # initialize the sum variable

response = input("Do you want to enter numbers? (yes/no): ")
while response.lower() == "yes":
    num_times = int(input("How many numbers do you want to add?: "))
    for i in range(num_times):
        num = int(input("Enter a number: "))
        total_sum += num
    response = input("Do you want to enter more numbers? (yes/no): ")

if response.lower() == "no":
    print("The total sum is:", total_sum)
else:
    print("Invalid input.")

total = 0
while True:
    response = input("Enter 'yes' to enter a number or 'no' to stop: ")
    if response == 'yes':
        num = int(input("Enter a number: "))
        total += num
    elif response == 'no':
        print("The sum of all input numbers is:", total)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


total = 0
while True:
    response = input("Enter 'yes' to enter a number or 'no' to stop: ")
    if response == 'yes':
        num = int(input("Enter a number: "))
        total += num
    elif response == 'no':
        print("The sum of all input numbers is:", total)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# find the GCD using Euclidean algorithm
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

# check if GCD is 1
if num1 == 1:
    print("The numbers are coprime.")
else:
    print("The numbers are not coprime.")
"""
start = 1
end = 10
sum_even = 0

for num in range(start, end+1):
    if num % 2 == 0:
        sum_even += num

print("The sum of all even numbers between", start, "and", end, "is", sum_even)
