import random
import string

def generate_password(length):
    if length < 4:
        return "❌ Password length must be at least 4 characters."

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = uppercase + lowercase + digits + symbols

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    print("==== Password Generator ====")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\n🔐 Your secure password: {password}")
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
