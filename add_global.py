var = 42


def add(number1):
    return(number1 + var)
    

def main():
    number1 = add(10)
    print("sum:", number1, "is a whole number")

if __name__ == '__main__':
    main()
