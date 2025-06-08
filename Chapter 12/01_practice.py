try:
    with (
        open("1.txt","r") as f1,
        open("2.txt", "r") as f2,
        open("3.txt", "r") as f3
        ):
        pass
except FileNotFoundError:
    print("These files doesn't exist.")
else:
    print("Files are ready to read.")
finally:
    print("Program successfully executed.")