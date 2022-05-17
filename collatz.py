#Chapter 3 Practice Project

def collatz(number):
    if number % 2 == 0:
        division_number = number //2
        print(division_number)
        return division_number
    elif number % 2 ==1:
        new_number = 3 * number + 1
        print(new_number)
        return new_number

thisBool = True
while(thisBool == True):
    user_input = input("please enter an integer number: ")
    try:
        int(user_input)
        thisBool = False
    except:
        thisBool = True