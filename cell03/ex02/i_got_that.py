user_input = input("What you gotta say? : ")
while True:
    if user_input.strip().upper() == "STOP":
        break
    print("I got that! Anything else? :", end=' ')
    user_input = input()
print("Goodbye!")