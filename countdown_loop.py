def while_counter(number):
    while number >= 0:
        print(number)
        number = number - 1

def for_counter(number):
    for count in  range(0,number, -1):
        print(count)

def main():
    counter = 10
    while_counter(counter)
    for_counter(counter)

if __name__ == '__main__':
    main()
