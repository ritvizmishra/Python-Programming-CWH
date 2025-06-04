from random import randint

class Train:
    def __init__(self, name):
        self.name = name
        
    # Book a ticket:
    def bookTicket(self, age, gender, phone):
        self.age = age
        self.gender = gender
        self.phone = phone
        
        print(f"Dear {self.name},\nConfirm your details: {self.name}, {age}, {gender}, {phone} [Y/N]")
        
    # Get status of the seats
    def getStatus(self):
        print(f"Number of available seats are {randint(150, 300)}.")
        
    # Get fare information
    def getFare(self):
        print(f"The fare for your ticket is {randint(500, 2000)}.")
        
passenger = Train("Ritviz Mishra")
passenger.bookTicket(24,'M',9288374839)
passenger.getStatus()
passenger.getFare()