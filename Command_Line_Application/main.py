THRESHOLD_LENGTH = 15

def is_palindrome(text):
    return text == text[::-1]

def is_all_lowercase(text):
    return text.islower() and text != ""

def is_all_digits(text):
    return text.isdigit() and text != ""

def is_longer_than_threshold(text, threshold=THRESHOLD_LENGTH):
    return len(text) > threshold

def is_empty(text):
    return text == ""

def print_menu():
    print("The available operations are:")
    print("1 - Palindrome: Check if the input is palindrome")
    print("2 - Lower: Check if all characters in the input are lowercase")
    print("3 - Digit: Check if all characters in the input are digits")
    print(f"4 - Long: Check if the input length is longer than {THRESHOLD_LENGTH}")
    print("5 - Empty: Check if the input is empty")
    print("6 - Exit: Exit successfully from the application")
    print()

def get_operation_choice():
    while True:
        try:
            return int(input("Please enter the number of the operation you choose: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.\n")

def get_user_input():
    return input("Enter an input: ")

def execute_operation(choice, user_input):
    if choice == 1:
        print(f"The answer is: {is_palindrome(user_input)}")
    elif choice == 2:
        print(f"The answer is: {is_all_lowercase(user_input)}")
    elif choice == 3:
        print(f"The answer is: {is_all_digits(user_input)}")
    elif choice == 4:
        print(f"The answer is: {is_longer_than_threshold(user_input)}")
    elif choice == 5:
        print(f"The answer is: {is_empty(user_input)}")
    elif choice == 6:
        print("Exit successfully")

def main():
    while True:
        print_menu()
        choice = get_operation_choice()
        if choice == 6:
            print()
            print("Exit successfully")
            break
        print()
        user_input = get_user_input()
        execute_operation(choice, user_input)
        print()

if __name__ == "__main__":
    main()