Функция print() - исполуется для вывода текст или каких то данных в консоль.   
The print() function is used to print text or some data to the console. 

Простой вывод строки.  
Simple string output.
# print("Hello word!") 
Описание: Эта строка кода вызывает функцию print(), которая выводит строку "Hello word!" в консоль.   
Description: This line of code calls the print() function, which prints the string “Hello word!” to the console. 


Вывод нескольких строк с разделением пробелами.  
Output multiple space-separated strings.
# print("Hello", "word!")
Описание: В этом случае print() принимает два значения: "Hello" и "word!".
По умолчанию функция print() вставляет пробел между передаваемыми значениями.  
Description: In this case print() takes two values: “Hello” and “word!”.
By default, print() inserts a space between the values passed in.

Изменение разделителя между выводимыми значениями.  
Change the separator between output values.
# print("Hello", "wold!", sep=", ")
Описание: Здесь используется параметр sep, который позволяет задать разделитель между значениями, передаваемыми в print(). 
В данном примере между "Hello" и "wold!" будет вставлена запятая с пробелом.  
Description: The sep parameter is used here to set the separator between the values passed to print(). 
In this example, a comma with a space will be inserted between “Hello” and “wold!”.

Вывод нескольких строк поочередно.  
Print multiple rows one by one.
# print("first row")
# print("second row")
Описание: Каждый вызов функции print() печатает текст и автоматически переходит на новую строку.  
Description: Each call to print() prints the text and automatically moves to a new line.

Вывод двух строк в одну.  
Output two lines into one.
# print("first row", end=" ")
# print("second row")
Описание: Обычно print() добавляет перенос строки в конце вывода, но параметр end=" " заменяет его на пробел.  
Description: Normally print() adds a line break at the end of the output, but the end=” ” parameter replaces it with a space.

Функция input() - приостановливает выполнение кода, чтобы пользователь что то ввел в терминал.  
The input() function - pauses code execution for the user to enter something into the terminal.

Получение данных от пользователя.  
Receiving data from the user.
# input("Please enter something")
Описание: Выводит текст "Please enter something" останавливает выполнение кода и ждет, пока пользователь введет что-то с клавиатуры и нажмет Enter.  
Description: Outputs the text “Please enter something” stops code execution and waits for the user to enter something from the keyboard and press Enter.

# name = input("Enter your name")
Описание: Выводит "Enter your name", принимает введенные данные и сохраняет их в переменную name.  
Description: Outputs “Enter your name”, accepts the input and saves it to the name variable.
# print(name)
Описание: Ожидает ввод И приглашением к вводу будет значение переменной name (то, что пользователь ввел раньше).  
Description: Waits for input and the prompt for input will be the value of the name variable (what the user entered earlier).