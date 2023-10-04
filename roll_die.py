import random
def main():
    # write your code here
    n = int(input("Enter the number of sides you would like your die to have:"))
    r = random.randrange(1, n)
    print('You have rolled a ',r, 'on your' ,n, 'sided die.')

    
    return

if __name__ == '__main__':
    main()