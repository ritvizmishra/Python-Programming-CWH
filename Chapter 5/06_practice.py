favLang = {}

for i in range(1,4):
    name = input("Enter your name: ")
    favLang[name] = input("Enter your favorite language: ")
    
print(favLang.items())
    
