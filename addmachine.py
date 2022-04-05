while True:
    try:
        first_number = int(input("What is the first number you want to add?"))
        second_number = int(input("What is the second number you want to add?"))
        sum = first_number + second_number
        print("The sum of your two numbers is", sum)
        break 
    except:
        print("You are so silly.  That is not an integer...")