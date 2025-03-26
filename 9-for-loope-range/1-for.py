# file_names = ["document.txt", "image1.jpg", "document2.txt", "image2.jpg"]

# for file_name in file_names:
#     print(file_name)       
# 
# Output:
# document.txt
# image1.jpg
# document2.txt
# image2.jpg


# greeting = "Hello, world"
# for char in greeting:
#     print(char)

# Output:
# H
# e
# l
# l
# o
# ,
 
# w
# o
# r
# l
# d


# greeting = "Hello, world"
# count_o = 0
# for char in greeting:
#     if char == "o":
#         count_o = count_o + 1
#         print(char)
# print(count_o)

# Output:
# o
# o
# 2

# students = ["Alice", "Dave", "Kara", "Jake"]

# for student in students:
#     print(student)
#     for char in student:
#         print(char)

# Output:   Можно сделать один вложенный цикл, а дальше программу нужно дробить.

# Alice
# A
# l
# i
# c
# e
# Dave
# D
# a
# v
# e
# Kara
# K
# a
# r
# a
# Jake
# J
# a
# k
# e


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# Output:

# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15


# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# for num in numbers:
#     if num == 10:
#         break

#     print(num)

# Output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Дальше программа вышла из цикла.