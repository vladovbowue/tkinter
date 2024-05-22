'''sum = 0
for i in numbers: #i=17 i=16 i=32 i=160 i=0
    a = len(str(i)) #160 -> '160' -> len('160') -> 3
    if a == 2 and i%8==0: #2==2->true 32%8==0->true
        sum = sum + i
print(sum)
while True:
    number = int(input('Введите число: '))
    numbers.append(number)
    if number == 0:
        break

print(numbers)
sum = 0
for i in numbers:
    if i >= 10 and i <= 99 and i%8 == 0:
        sum = sum + i
print(sum)'''
'''
s = '1sdf'
a = s.replace('world', 'мир')
b = a.replace('hello', 'привет')
c = s.split(' ')
#print(c)
#print(s.isalpha()) #метод возращает True если в строке присутствуют только буквы или цыфры, False в противном случае
#print(s.isdigit())
''''''
chislo = input('Введите число: ')
if chislo.isdigit():
    print('В ваше строке находятся только числа')


'''
'''
f = open('users.txt', 'r')
users_new_s = []
users = f.readlines()
for user in users:
    users_new_s.append(user.replace('\n', ''))
f.close()
print(users_new_s)

login = input('Login: ')
password = input('Password: ')

for user in users_new_s:
    user_n = user.split(':')
    if user_n[0] == login and user_n[1] == password:
        print('Вы аторизировались')'''

'''f = open('users.txt', 'w')
f.write('user4:12345')
f.close()'''
'''
f = open('users.txt', 'a')
login = input('Login: ')
pasword = input('Password: ')
r = '\n'+login+':'+pasword  #user11:12345
f.write(r)
f.close'''

'''
1 + 2 = 3
'1'+'2'='12'
'''



#создать список из числовых значений, которые нужно брать из файла. 1. Найти минимальный и максимальный элемент этого списка. 2. Найти сумму и среднее арифметическое значение этих элементов
#среднее арифметическое = сумма всех элементов / кол-во элементов в списке len

n = open('s.txt', 'r')
s = n.readlines()
new_s = []
for i in s:
    new_s.append(int(i.replace('\n','')))
n.close()
print("Минимальное значение:", min(new_s))
print("Максимальное значение:", max(new_s))
print("Среднее арифметическое:", round(sum(new_s)/len(new_s)))



