def main():
    # write your code here
    for number in range (1, 11):
        print("The multiplication table for", number, "is: ")
        for column in range(1, 11):
            print(number, "x", column, "=", number * column)

    return

if __name__ == '__main__':
    main()