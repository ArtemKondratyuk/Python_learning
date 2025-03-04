Простая переменная.  
Simple variable.
# name = "Alice"
# print(name)   # output: Alice
Описание: Переменная name хранит строку "Alice", и print(name) выводит её.  
Description: The variable name stores the string “Alice”, and print(name) outputs it.

Несколько переменных.  
A few variables.
# name = "Alice"
# age = 25
# print(name, age)     # output: Alice 25
Описание:Можно хранить несколько значений в разных переменных и выводить их через запятую — print() автоматически вставляет пробел.  
Description: You can store few values in different variables and output them comma-separated - print() automatically inserts a space.

Короткое присваивание.  
Short assignment.
# name, age = "Alice", 25
# print(name, age)     # output: Alice 25
Описание: Можно объявлять несколько переменных в одной строке. name получит "Alice", age — 25.  
Description: You can declare few variables on the same line. name will get “Alice”, age will get 25.

Копирование переменной.  
Copying a variable.
# name = "Alice"
# other_name = name

# print(other_name)    # output: Alice 
Описание: other_name теперь ссылается на ту же строку, что и name. Оба хранят "Alice".  
Description: other_name now references the same string as name. Both store “Alice”.

Обмен значений без временной переменной.  
Value exchange without a temporary variable.
# x = 3
# y = 4

# x, y = y, x
# print(x, y)     # output: 4 3
Описание: Классический своп в Python. x и y меняются местами без лишних переменных.  
Description: Classic swap in Python. x and y are swapped without extra variables.  

Определение типа переменной.  
Defining the type of a variable.
# variable = 1
# print(type(variable))  # output: <class 'int'>

# variable = "Hello world!"
# print(type(variable))    # output: <class 'str'>
Описание: Функция type() показывает, к какому классу относится переменная. Можно динамически менять её тип.  
Description: The type() function shows to which class a variable belongs. You can dynamically change its type.

Ошибка из-за переопределения print.  
Error due to overriding print.
# print = 1
# print(1)    # Don't do that!!!  output: Error
Описание: Нельзя использовать print как имя переменной. Иначе потеряешь встроенную функцию print(), и вызов print(1) вызовет ошибку.  
Description: You must not use print as a variable name. Otherwise you will lose the built-in print() function, and calling print(1) will cause an error.

Используй осмысленные имена переменных, следи за их типами и не переопределяй встроенные функции.  
Use meaningful variable names, watch their types, and don't override built-in functions.