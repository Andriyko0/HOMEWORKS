#1
given_string = '    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   '
print(given_string[4:-3])#1.1
print("    i am gonna have my super power tomorrow morning so i am heading to bed now. Bye everyone   ".count('a'))#1.2
print(given_string.upper()) #1.3
print(given_string.lower()) #1.4
s = given_string
if s.isalpha():
     print('Цей рядок містить лише літери')
else:
    print('Тут не тількі літери')#1.6
print(given_string.replace('super power','tasty breakfast'))#1.6
print(given_string.replace(" ","-").replace("i","1"))#1.7
print(given_string.replace('super power','tasty breakfast').upper().replace("i","1").replace(" ","-")[4:-3])#1.8
#2
pasvord = input('Уведіть пароль ')
g = pasvord
if len(pasvord) < 8:
    print("В паролі має бути хочаб 8 символів !")
elif g.isalpha():
    print('В паролі лишень літери та букви')

#3
while True:
    s = input("Знак (+,-,*,/): ")

    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Ділення на нуль!")
    else:
        print('Це точно знак?')