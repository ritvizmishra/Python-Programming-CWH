class Programmer:
    company = "Microsoft data:"
    def employeeInfo(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        
        print(f"{name}'s email is {email} and he is {age} years old.")
        
employee1 = Programmer()
print(employee1.company)
employee1.employeeInfo("Ritviz Mishra", "xyz@ms.com", 24) 