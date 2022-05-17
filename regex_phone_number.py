import re #import regex here

number = input("what is your phone number? \n") #creating a variable that takes an input
try: #starting a try here
    phone_num = re.compile(r'(\d{3})-(\d{3}-\d{4})') #create a variable named phone_num the compiles a raw string (r) looking for first 3 digits discarding a - and then 3 digits a - and 4 digits
    match = phone_num.search(f'{number}') #creating a variable that will put a string into the search function of phone_num
    print(match.group(1)) #printing the first group of 3 digits
    print(match.group(2)) #printing the second group of 3 digits, a - and 4 digits
    print(match.groups()) #printing both first and second group.
    area_code, main_number = match.groups() #because the groups seperates the values into a tuple we can assign them to different variables.
    print(area_code)
    print(main_number)
except: #if they do not put in the phone number correctly.
    print("Please use the format 123-123-1234")

try:
    phone_num = re.compile(r'(\d{3}-\d{3}-\d{4})') #create a variable named phone_num the compiles a raw string (r) with NO GROUPS, as in just one thing inside a parentheses
    match = phone_num.findall(f'{number}')# will find multiple instances of numbers
    print(match)
except:
    print("Please use the format 123-123-1234")