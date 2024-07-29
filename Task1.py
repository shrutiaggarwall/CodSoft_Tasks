import string
import random

def generate_password(length):
    str1 = string.ascii_lowercase
    str2 = string.ascii_uppercase
    str3 = string.digits
    str4 = string.punctuation

    s = []
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))

    random.shuffle(s)

    return "".join(s[0:length])

if __name__ == "__main__":
    while True:
        L = int(input("Enter password length\n"))
        print("Your generated password:")
        print(generate_password(L))
        
        choice = input("Do you want to generate another password? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the password generator!")
            break

