def display_menu(my_list):
    my_list = {1: "Hello", "Hi": 25, "Howdy": 100}

print(1 in my_list) # True


print("Howdy" not in my_list) # False

print("Hello" in my_list) # False

def main():
    display_menu()

if __name__ == '__main__':
    main()
