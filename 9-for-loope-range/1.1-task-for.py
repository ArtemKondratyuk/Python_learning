# Задача: Напиши программу, которая выводит все чётные числа от 1 до 20 (включительно). 
# Для каждого чётного числа нужно выводить строку в формате: "Число X чётное".  
# Task: Write a programme that outputs all even numbers from 1 to 20 (inclusive). 
# For each even number you need to output a string in the format: ‘Number X is even’.  

# 1 вариант решения.  
# 1 decision option.
# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# text = "is even."
# for num in numbers:
#     if num % 2 == 0:
#         print(num, text)

# Output:

# 2 is even.
# 4 is even.
# 6 is even.
# 8 is even.
# 10 is even.
# 12 is even.
# 14 is even.
# 16 is even.
# 18 is even.
# 20 is even.

# 2 упращенный вариант решения спомощью функции range 
# которая позволяет генерировать последовтельность чисел.
# 2 an improved version of the solution using the range function 
# which allows you to generate a sequence of numbers.

# text = "is even."
# for num in range(1, 21):
#     if num % 2 == 0:
#         print(num, text)

# Output:

# 2 is even.
# 4 is even.
# 6 is even.
# 8 is even.
# 10 is even.
# 12 is even.
# 14 is even.
# 16 is even.
# 18 is even.
# 20 is even.


# Задача: Напиши программу, которая суммирует все нечётные числа от 1 до 50 (включительно) и выводит результат.
# Task: Write a program that sums all odd numbers from 1 to 50 (inclusive) and outputs the result.

# sum = 0
# for num in range(1, 51):
#     if num % 2 != 0:
#         sum += num

# print(sum)

# Output:  625