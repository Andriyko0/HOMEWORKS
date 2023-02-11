#1
while True:
    FAMILI =[
        {"name": "Jylia","rule":"Mom"},
        {"name": "Volodumr", "rule":"Ded"},
        {"name": "Andrue", "rule": "Sone"}
        ]
#2
    for contact in FAMILI:
        numer = 0
        print(f"{contact['name']}")
        numer += 1
#2.1
    for contact in FAMILI:
        numer = 0
        print(f"{contact['name']}:{contact['rule']}")
        numer += 1
    #3
    name = input("Input name ")
    numer = 0
    for contact in FAMILI:
        if contact["name"] == name:
            print(f"{contact['name']}:{contact['rule']}")
            numer += 1
    break
#4
import random
str1 = []
while len(str1)<=20:
    str1+=str(random.randint(10,100))
print(str1)
