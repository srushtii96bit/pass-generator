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