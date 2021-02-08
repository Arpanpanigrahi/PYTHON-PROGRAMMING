#3. Create a custom exception

class Error(Exception):
    pass
class VaueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass
number=25
while True:
    try:
        num = int(input("Enter a Number:"))
        if num < number:
            raise VaueTooSmallError
        elif num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value is too small please try again")
        print()
    except ValueTooLargeError:
        print("Value is too large please try again")
        print()
print("Guessed value is correct")
        
            
