print("Give me two numbers, and I'll add them!")
print("Enter 'q' if you want to quit.")

while True:
    num1 = input("\nEnter the first number: ")
    if num1 == 'q':
        break
    num2 = input("Enter the second number: ")
    if num2 == 'q':
        break

    try:
        sum = int(num1) + int(num2)
    except ValueError:
        print("\nDon't you know what numbers are? Try entering two numbers.")
    else:
        print("The sum of " + num1 + " and " + num2 + " is " + str(sum) + ".")