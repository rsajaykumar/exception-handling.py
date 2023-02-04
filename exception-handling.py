#events detected during the execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    
except ZeroDivisionError as e:
    print(e)
    print("You cannot divide by 0")
    
except ValueError as e:
    print(e)
    print("Plz enter only number!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally:
    print("The will always execute: ",result)