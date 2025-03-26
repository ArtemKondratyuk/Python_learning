Основные операции с числами.  
Basic operations with numbers.  

Сложение.  
Addition.   
# x = 10
# y = 5
# summary = x + y

# print(summary)
Описание: Сложение целых чисел (int).
Description: Addition of integers (int).



# x = 10.5
# y = 5.5
# summary = x + y

# print(summary)
Описание: Сложение чисел с плавающей запятой (float).  
Description: Adds floating point (float) numbers.  

Умножение.  
Multiplication.
# x = 10
# y = 5
# z =  x * y

# print(z)

Деление.  
Division.
# x = 10
# y = 5
# z =  x / y

# print(z)


Возведение в степень.  
Elevation in degree.
# x = 2
# print(x ** 3)


Целочисленное деление.  
Integer division.
# x = 9
# y = 4
# print(x // y)


Остаток от деления.  
Residue of division.
# x = 9
# y = 4
# print(x % y)


Приоритет операций.  
Prioritize operations.
# integer = 2 + 3 * 5
# print(integer)
Описание: Без скобок умножение (*) выполняется раньше сложения (+).  
Description: Without parentheses, multiplication (*) is done before addition (+).


# integer = (2 + 3) * 5
# print(integer)
Описание: Скобки меняют приоритет.  
Description: Brackets change the priority.


Огромные числа.  
Huge numbers.
# biger_number = 10 ** 1000
# print(biger_number)
Описание: Можно работать с большими числами, потому что int в нем имеет неограниченную длину (ограничен только памятью компьютера).
Description: You can work with large numbers because int in it has unlimited length (limited only by computer memory).


Преобразование типов.  
Type conversion.
# my_int = 1
# my_float = float(my_int)
# print(my_float)          # output: 1.0
Описание: Целое в float.  
Description: Integer in float.


# my_float = 1.5
# my_integer = int(my_float)
# print(my_integer)        # output: 1
Описание: float в целое (отбрасывает дробную часть).  
Description: float to integer (discards fractional part).


# my_float = 1.999999
# my_integer = round(my_float)
# print(my_integer)        # output: 2
Описание: Округление.   
Description: Roundup.



Задание.  
Task.  

В высотном доме 5 подъездов по 20 квартир каждый. На каждом этаже 4 квартиры. Нумерация квартир идёт подряд, снизу вверх:  
на 1м этаже, 1го подъезда находятся квартиры 1, 2, 3, 4.  
на 2м этаже, 1го подъезда находятся квартиры 5, 6, 7, 8 и т.д.  
Напишите скрипт, который получает номер квартиры и выводит на экран номер подъезда и этажа.  
Протестируйте скрипт на разных значениях входных данных.  
A high-rise building has 5 floors with 20 apartments each. There are 4 apartments on each floor. The apartments are numbered consecutively, from bottom to top:  
on the 1st floor of the 1st entrance there are apartments 1, 2, 3, 4.  
On the 2nd floor of the 1st entrance there are apartments 5, 6, 7, 8, etc.  
Write a script that gets the apartment number and displays the entrance and floor number on the screen.  
Test the script on different values of input data.

Решение:  
Solution:  

# flat_number = 9
# entrance_number = 1 + (flat_number - 1) // 20
# floor_number = 1 + (flat_number - 1) % 20 // 4

# print("Entrance_number: ", entrance_number)
# print("Floor number: ", floor_number)