Работа лочического значения (bool), операциями сравнения и логическими операциями:  
The operation of bool, comparison and logical operations:

Переменные типа bool.  
Variables of type bool.  
# is_student = True
# is_graduated = False

# print(is_student)      # output: True 
# print(is_graduated)   # output: False



Сравнение чисел (==).  
Comparison of numbers (==).
# x = 10
# y = 10
# print(x == y)   # output: True

# x = 9
# y = 10
# print(x == y)  # output: False 



Сравнение с присвоением результата.  
Comparison with result assignment.
# x = 10
# y = 10

# is_equal = x == y
# print(is_equal)

# x = 10
# y = 10

# not_equal = x != y
# print(not_equal)    # False

# x = 9
# y = 10

# not_equal = x != y
# print(not_equal)     # True



Операторы >, <, >=, <=.  
Operators >, <, >=, <=.
# x = 10
# y = 9

# print(x > y)     #True
# print(x < y)     #False
# print(x >= y)    #True
# print(x <= y)    #False




Логические операторы and, not.  
Logical operators and, not. 
# x = 1
# print(x < 5 and x > -2)    #True

# x = 6
# print(x < 5 and x > -2)    #False

# is_tudent = True 
# print(not is_tudent)       #False



Функция bool().  
The bool() function.
# print(bool(1))    #True
# print(bool(0))    #Falsre
# print(bool(-1))   #True
# print(bool("Hello, world!"))   #True
# print(bool(""))   #False