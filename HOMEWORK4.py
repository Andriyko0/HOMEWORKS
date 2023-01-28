#1
password = input("You password ")
lower=False
upper = False
len1 = False
simwol = False
while True:
    if password in password.lower():
        lower = True
    if password in password.upper():
        upper = True
    if len(password) >= 8:
        len1 = True
    if  password in ["#","&","%",]:
        simwol = True
    else:
       break
if len1 and simwol and upper and lower:
    print(password)
if upper == False or lower == False:
    print("Перевір наявнісьть двох регістрів ")
if simwol == False or len1 == False:
    if simwol == False:
        print("Тут нема символів")
    elif len1 == False:
        print("Занадто короткий")
# #2.1
# value1 = int(input("Уведіть число "))
# zero1 = 0
# while zero1 <= value1:
#     print(zero1)
#     zero1 +=1
# #2.2
# value2 = int(input("Уведіть число "))
# zero2 = 0
# while zero2 <= value2:
#     if zero2%2 == 0:
#         print(zero2)
#     zero2+=1
# #2.3
# value3 = int(input("Уведіть число "))
# zero3 = 0
# while zero3 <= value3:
#     if zero3%3 == 0 and zero3%4 == 0 :
#         print(zero3)
#     zero3+=1
#
# #3.1
# value1 = int(input("Уведіть число "))
# zero1 = 0
# while True:
#     print(zero1)
#     zero1 +=1
#     if zero1 == value1+1:
#         break
# #3.2
# value2 = int(input("Уведіть число "))
# zero2 = 0
# while True:
#     if zero2%2 == 0:
#         print(zero2)
#     zero2+=1
#     if zero2 == value2+1:
#         break
# #3.3
# value3 = int(input("Уведіть число "))
# zero3 = 0
# while True:
#     if zero3%3 == 0 and zero3%4 == 0 :
#         print(zero3)
#     zero3+=1
#     if zero3 == value3+1:
#         break

#4
# text = "You only get one shot, do not miss your chance to blow This opportunity comes once in a lifetime"
# index = 0
# letter = input(" ")
# while letter in text:
#     if text[index] == letter:
#         index +=1
#         continue
#     print(text[index])
#     index += 1



