# pass-generator
Simple Pass generator


import random
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits = list("0123456789")
symbols = list("!@#$%^&*")

print("-- SIMPLE DYNAMIC PASSWORD GENERATOR --")

while True:
    print(" Choose strength:")
    print("1. Weak (letters only)")
    print("2. Medium (letters + numbers)")
    print("3. Strong (letters + numbers + symbols)")

    choice = int(input("Enter choice (1-3): "))
    if choice < 1 or choice > 3:
        print("Invalid choice! Please choose between 1 and 3.")
        print("Code Ended!!.")
        break
    length = int(input("Enter password length , length: "))

    chars = []

    if choice == 1: 
        chars = letters
    elif choice == 2:
        chars = letters + digits
    elif choice == 3:
        chars = letters + digits + symbols
    else:
        print("Generating password...")

    password = "  "

    for i in range(length):
        password += random.choice(chars)

    print("Your Password:", password)

    again = input("should i Generate again? -- (y/n): ")
    if again != 'y':
        print("Code Ended!!.")
        break 
        
  Sample Output
-- SIMPLE DYNAMIC PASSWORD GENERATOR --

Choose strength:
1. Weak (letters only)
2. Medium (letters + numbers)
3. Strong (letters + numbers + symbols)

Enter choice (1-3): 3
Enter password length: 8

Your Password: A7@kP#2m

Should I generate again? (y/n): y
