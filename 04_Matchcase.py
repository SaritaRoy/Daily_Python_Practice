a = int(input("Enter a  number between 1 and 10: "))

match a :
    case 1:
        print("You won a charger")
    case 2 :
        print("The value is $3")
    case 3 :
        print("You won a camera")
    case _:
        print("Better luck next time")
    
#match case is a new features introduced in python 3.10 for pattern matching.
#it simplifies complex condition logic.
