3 способа как развернуть list:
3 ways how to deploy a list:

1 Способ:
1 Way:
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[::-1]
# print(new_numbers)

2 Способ:
2 Way:
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.reverse()
# print(numbers)

3 Способ:
3 Way:
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = list(reversed(numbers))
# print(type(new_numbers))
# print(new_numbers)


Работа с индексами в списках.  
Working with indexes in lists. 

Обращение к элементам списка по индексу.
Accessing list items by index.
# fruits = ["apple", "banana", "cherry", "watermelon"]

# print(fruits[0])
# print(fruits[-4])       # apple   aplle 
Описание: Оба дают первый элемент(тоесть нулевой, так как счет начинается с нуля).  
Description: Both give the first element(i.e. zero, since counting starts from zero). 

# fruits = ["apple", "banana", "cherry", "watermelon"]

# print(fruits[4])        # Error

# print(fruits[-5])       # Error
Описание: Оба вызывают ошибку (индексы выходят за границы списка).  
Description: Both cause an error (indexes go outside the list boundaries).  

Изменение элементов по индексу.  
Changing elements by index. 


# fruits = ["apple", "banana", "cherry", "watermelon"]
# fruits[0] = "penapple"

# print(fruits)       #   ['penapple', 'banana', 'cherry', 'watermelon'] 
Описание: Заменяет первый элемент.  
Description: Replaces the first element. 

# cars = ["Ferrari", "Audi", "Volkswagen"]
# cars[1] = "BMW"

# print(cars)      #  ['Ferrari', 'BMW', 'Volkswagen']


# names = ["Sten", "Jordan", "Jefro", "Ted"]
# names[3] = "Scot"

# print(names)      #  ['Sten', 'Jordan', 'Jefro', 'Scot']


Обмен значений в списке.  
Exchanging values in a list. 
# names = ["Sten", "Jordan", "Jefro", "Ted"]
# names[1], names[3] = names[3], names[1]

# print(names)    # ['Sten', 'Ted', 'Jefro', 'Jordan']
Описание: Меняет местами элементы по индексам.  
Description: Swaps elements by index. 



Срезы списков (list[start:stop:step]).  
List slices (list[start:stop:step]). 

Срез по диапазону(берём часть списка).  
Range cut (take a part of the list). 
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[0:5])          # [1, 2, 3, 4, 5] 

Срез с середины списка.  
A cut from the middle of the list.
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(numbers[3:9])          # [4, 5, 6, 7, 8, 9]


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[2:6]

# print(new_numbers)      #  [3, 4, 5, 6]


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[0:10]

# print(new_numbers)    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


Копирование списка.  
List Copying.  
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[:]

# print(new_numbers)    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Описание: Если start и stop не указаны, берётся весь список.  
Description: If start and stop are not specified, the entire list is taken. 

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[0:len(numbers)]

# print(new_numbers)    #  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


Пропускаем элементы (с шагом 2).  
Skip elements (in increments of 2).  
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[0:10:2]

# print(new_numbers)      #  [0, 2, 4, 6, 8]


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[::2]

# print(new_numbers)      #   [0, 2, 4, 6, 8]


Разворачиваем список.  
Unfolding the list.
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_numbers = numbers[::-1]

# print(new_numbers)      #  [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]