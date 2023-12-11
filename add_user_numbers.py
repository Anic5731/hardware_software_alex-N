var = 42
def ask_me():
    number = int(input("enter number:"))
    return(number)

def add(number):
    return(number + var)

def main():
    number1 = ask_me()
    number2 = ask_me()

    sum = add(number1)
    sum = add(number2)


    print("sum:", sum)
    print("Global:",number1 + var)

if __name__ == '__main__':
    main()
