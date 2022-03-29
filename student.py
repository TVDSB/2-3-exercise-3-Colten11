def main():
    #your code goes here
    number = float(input("Enter a number: "))
    if number%3 == 0 and number%5==0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)

if __name__ =='__main__':
    main()
