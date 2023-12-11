def user_selection():
    while True:
        print("1. Option 1")
        print("2. Option 2")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':

            print("You selected Option 1.")
        elif choice == '2':

            print("You selected Option 2.")
        elif choice == '3':
            print("Quitting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    user_selection()

if __name__ == '__main__':
    main()
