def decimal_to_binary(decimal_number):
    binary_result = bin(decimal_number)[2:]
    return binary_result

def binary_to_decimal(binary_number):
    decimal_result = int(binary_number, 2)
    return decimal_result

def main():
    print("Welcome to the Decimal-Binary Converter!")
    print("This program can convert a decimal number to binary and a binary number to decimal.")

    while True:
        print("Choose an option:")
        print("1. Convert Decimal to Binary")
        print("2. Convert Binary to Decimal")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            decimal_input = int(input("Enter a decimal number: "))
            binary_output = decimal_to_binary(decimal_input)
            print(f"The binary representation of {decimal_input} is: {binary_output}")

        elif choice == '2':
            binary_input = input("Enter a binary number: ")
            decimal_output = binary_to_decimal(binary_input)
            print(f"The decimal representation of {binary_input} is: {decimal_output}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
