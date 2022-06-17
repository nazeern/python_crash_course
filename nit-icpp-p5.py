#Finding whether number is divisible by 4, 9, or neither
print "Checking dvisibility of a number by 4 and 9"
number = int(raw_input("Enter the number : "))
if number%4 == 0 and number%9 == 0:
    print "%d is divisible by both 4 and 9" %number
elif number%4 == 0:
    print "%d is divisible only by 4, not by 9" %number
elif number%9 == 0:
    print "%d is divisible by 9, not by 4" %number
else:
    print "%d is not divisible by 4 or 9" %number
