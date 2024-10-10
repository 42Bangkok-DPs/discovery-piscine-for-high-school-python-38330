first = int(input("Enter the first number:\n"))
second = int(input("Enter the second number\n"))
answer = first * second
print(f"{first} x {second} = {answer}")
if answer > 0 : print("The result is possitive.")
elif answer < 0 : print("The result is negative.")
else : print("The result is possitive and negative.")