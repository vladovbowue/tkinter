
'''
Name: Вася
phone: 234235235

print('привет мир')
print(10 + 20)
print(30 - 10)
print(10 * 4)
print(40 / 10)
print(100 // 30)
print(100 % 30)
print(18 % 2)
print(56 % 5)
print(2 ** 8)

#строковый тип данных
name = 'Вася' #инициализация переменной

print(name)

#числовой тип данных
a = 10
b = 40
c = 5.4
print(a + b + c) #55.4
print(a ** 3 + b ** 3 + c ** 3)

#логический тип данных

i = True #False


#name = 'Вася'
#print('Привет, ' + name)

name = input('Ваше имя: ')
print('Привет, ' + name)


#условная конструкция if
age = 20
if age > 30: #True
    print('Ок')
else:
    print('No')
name = input('Ваше имя: ')
age = int(input('Ваш возраст: ')) # '20' 20
if age > 18:
    print('Вы авторизировались в системе')
    login = input('Login: ')
    password = input('Password: ')
    if login == 'admin' and password == 'admin':
        print('Вы авторизировались как админ')
else:
    print('Вы не подходите по возрасту')


and(логическое умножение)
False(0) False(0) -> False(0)
False(0) True(1) -> False(0)
True(1) False(0) -> False(0)
True(1) True(1) -> True(1)

or(логическое сложение)
False(0) False(0) -> False(0) 
False(0) True(1) -> True(1)
True(1) False(0) -> True(1)
True(1) True(1) -> True(1)

отрицание
False -> True
True -> False
'''
#print(not 10 == 10) #False


#циклы
#for, while
'''i = 0
while i < 10:#true true  10 < 10 -> false
    print(i)#0 1    
    i = i + 1 #i+=1   i=1   i=2

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f'{j} * {i} = {i * j}', end='\t')
        #print(str(i) + " * " + str(j) + " = " + str(i * j),end='\t')
        j += 1
    print()
    i += 1


#д/з найти сумму всех чисел от 0 до 100 
print('sdsdg', end='\t')
print('sdgsdg')
a = 0

#i=0
#while i <= 100:
    #print(i)
    #i = i + 1
#else:
s = 0
i = 0
while i <= 100: #первая итерация цикла i = 0 0 <= 100    торая итерация цикла i = 1  1 <= 100   i = 2 i = 3 .... i = 100
    s = s + i #s=0+1=1  s=1+1=2 s=2+2=4 s=4+3=7 s=7+4=11 ...
    i = i + 1 #i = 0 + 1 = 1    i = 2   i = 3 i =4 ... i = 100
#sum(s+s)
#print(s)


i = 0
while i < 5:#0 < 5 (true)  1 < 5 (true) 2 < 5(true) ... 4 < 5(true)  5 < 5 (false)
    #print(i)#0 1 2 3 4

    i = i + 1#i=1 i=2 i=3 i=4 i=5

#for
#список(list)
a = 10
b = [3, 6, 4, 5, 6, 10]
#    0  1  2  3  4   5
print(b[3])
print(b[5])
users = ['user1', 'user2', 'user3', 'user4', 'user5']
print(users[2])
print(users[-1])
for user in users:
    print(user)


d = [5, 10, 34, 12, 10]
for i in d: #i=5 i=10 i=34 i=12 i=10
    if i%2 == 1: #1==0(false) 0==0(true)
        print(i)

f = [4, 3, 10, 3, 'hello', False]
#    0  1   2  3    4       5
print(f[4])
for i in f:
    print(i)


index = 0
while index < 6:
    print(f[index])
    index = index + 1


for i in range(0, 100, 2):
    print(i)

'''
'''

users = ['user1', 'user2', 'user3', 'user4', 'user5', 'user6']
print(len(users))

users.append('user7') #добавляет элемент 'user7' в конец списка
print(users)
users.append('user8')
print(users)

users.insert(1, 'user9') # добавляет элемент в список по индексу
print(users)
users.insert(0, 'user10')
print(users)

users.remove('user7') #удаляет элемент по значению

#users.clear()

print(users.count('user10')) #возвращает кол-во вхождений элемента в список

users.sort()

print(users)

users.sort(reverse=True) #сортировка элементов списка по убыванию
print(users)

users_new = users.copy() #копируем список

print(users_new)

index = users.index('user1') #возвращает индекс элемента. Если элмент не найден, программа генерериет ошибку(исключение)
print(index)

a = [1,4,5,3,4,10,14]
print(max(a)) #14
print(min(a)) #1
print(sum(a)) #

#in
if 5 in a: #true
    print('Yes')

del a[-1]
print(a)
'''
#создать список из числовых значений. 1. Найти минимальный и максимальный элемент этого списка. 2. Найти сумму и среднее арифметическое значение этих элементов
#среднее арифметическое = сумма всех элементов / кол-во элементов в списке len()

'''i = [5,6,35,23,1,2,3,4,65]
print("Минимальное значение:",min(i))
print("Максимальное значение:",max(i))
print("Среднее арифметическое:",sum(i)/len(i))
'''
