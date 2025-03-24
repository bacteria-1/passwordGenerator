import random
import string

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    # Ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    
    password += [random.choice(characters) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)

def save_password(password):
    save_option = input("How would you like to save your password? (Enter filename or 'none'): ").strip()
    if save_option.lower() != 'none':
        with open(save_option, 'w') as file:
            file.write(password)
        print(f"Password saved to {save_option}")
    else:
        print("Password not saved.")

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be greater than zero.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    use_upper = get_yes_no_input("Include uppercase letters? (yes/no): ")
    use_digits = get_yes_no_input("Include numbers? (yes/no): ")
    use_symbols = get_yes_no_input("Include special characters? (yes/no): ")
    
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"Generated Password: {password}")
    
    save_password(password)

if __name__ == "__main__":
    main()