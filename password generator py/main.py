import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator App!")
    
    # Get user input for password criteria
    length = int(input("Enter the desired password length: "))
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
