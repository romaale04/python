# типы данных
# int, float, booleam=n, str, list, None
# value = None
# print(type(value))
# print(type(a))
# print(type(b))
# print(type(value))
# f = False
# print(f)
# list = ['1', '2', '3', ]
# col = ['hello world', 1,2,4.5,True]
# print(list)
# print(col)


# a = 123
# b = 1.23
# value = 12334
# s = 'hello "world'

# print(s) # вывод строки
# print(a, ' - ', b, ' - ', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# Ввод и вывод данных
# print, inrut

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float (input())
# print(a, ' + ' , b, ' = ', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')


# Арифметические операции
# +, -, *, /, %, //, **
# **, *, /, //, %, +, -
# (), Сокращенные операции
# a = 3
# a *= 5

# print(a)



# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# f = [1,2,3,4]
# # print(f)
# # print(not 2 in f)

# is_odd = not f[0] % 2 
# print(is_odd)



#Управляющие конструкции
# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!') 
# elif   username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif  username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username )

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит)')
# print(inverted)


# Управляющие функции:
# for


# for i in 'qwerty':
#     print(i)



text = 'съешь ещё этих мягких французских булок'


print(len(text))
print('ещё' in text)
print(text.isdigit())
print(text.islower())
print(text.replace('ещё', 'ЕЩЁ'))

for c in text:
    print(c)
