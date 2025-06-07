'''
-> Why Handle Exceptions?
    So that your program doesn’t crash, and you can respond gracefully (e.g., show a message, retry, log the error).

-> Basic Structure of Exception Handling
    try:
        # risky code here
    except SomeError:
        # what to do if error happens
    else:
        # optional: runs if no error occurs
    finally:
        # optional: always runs (even if error happens)
        
-> Common exceptions:
| Exception           | When it happens                       |
| ------------------- | ------------------------------------- |
| `ZeroDivisionError` | Dividing by zero                      |
| `ValueError`        | Wrong value type (e.g., `int("abc")`) |
| `TypeError`         | Wrong operation on the wrong type     |
| `FileNotFoundError` | File doesn’t exist                    |
| `IndexError`        | List index out of range               |
| `KeyError`          | Missing key in dict                   |

--> Custom Exceptions:
You can even define your own:
    class TooYoungError(Exception):
        pass

    def check_age(age):
        if age < 18:
            raise TooYoungError("You must be 18+")
'''

# Example:
try:
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Enter a valid number!")
else:
    print("Number successfully divided!")
finally:
    print("Thankyou for using me!")