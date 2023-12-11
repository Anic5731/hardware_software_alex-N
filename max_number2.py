def max(number1, number2):
    if number1 >= number2:
        print("1:" ,number1)
        return number1
    print("2:" ,number2)
    return number2

def main():
    larger = max (1,5)
    print(larger)

if __name__ == '__main__':
    main()
