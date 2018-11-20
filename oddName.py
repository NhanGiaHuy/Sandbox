
def main():
    user_name = str(input("Enter your name: "))
    while len(user_name) <= 0:
        print("the name cannot be blank")
        user_name = str(input("Enter your name: "))
    for position in range(1, len(user_name), 2):
        print(user_name[position], end="")


main()