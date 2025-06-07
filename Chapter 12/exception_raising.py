'''
Minimum age: 18
Maximum age: 80
Anything outside this range should raise a custom exception.
'''
class UserNotEligible(Exception):
    pass

def checkEligibility(age):
    if age < 18 or age > 80:
        raise UserNotEligible("You're not eligible")
    else:
        print("Here's your license.")
        
try:
    age = int(input("Enter your age: "))
    checkEligibility(age)
except UserNotEligible as na:
    print(f"{na}")
finally:
    print("Process done.")
    