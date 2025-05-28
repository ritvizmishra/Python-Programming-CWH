# Checking for prime num

num = int(input("Enter the num to check: "))

if num < 2:
    print(f"{num} is neither prime nor composite.")
elif(num == 2):
    print("2 is a prime number.")
else:
    for i in range(2,int((num**0.5)+1)):
        if(num % i == 0):
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")

    
    
