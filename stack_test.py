def stack_me_high(number1):
    if number1 == 100:
        return number1
    print("current count:" ,number1)
    number1 += 1
    stack_me_high(number1)

def main():
    number1 = stack_me_high(1)
    print( "current count:" , number1)

if __name__ == '__main__':
    main()
