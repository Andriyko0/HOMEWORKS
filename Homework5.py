#1
number_to_ad = 0
gost_list = []
while number_to_ad <= 100:
    gost_list.append(number_to_ad)
    number_to_ad += 1
print(gost_list)
#2
index2 = 0
sum = 0

while len(gost_list)-1 >= index2:
    sum += gost_list[index2]
    index2 += 1
print(sum)
#3
given_list = [False, 0, 'str', '123', 'hello', '%', 1.2, 1]
a1sda = 0
while a1sda < len(given_list):
    print(type(given_list[a1sda]))
    a1sda+=1
#4
a = [1, 2, 5, 2, 4, 1, 0,] #Щоб працювало
b = [4, 3, 1, 2]
index3 = 0
max_value = 0
while len(a) > index3:
    print(a[index3])
    if max_value < a[index3]:
        max_value = a[index3]
    index3 += 1
print(f"Макс {max_value}")
index4 = 0
min_value = 0
while len(a) < index4:
    if max_value > a[index4]:
        max_value = a[index4]
    index4 += 1
print(f"Мін {min_value}")
c = []
for i in a:
   for j in b:
       if i == j:
           c.append(i)
           break
print(c)

