numbers_list = [10, 15, 3, 7, 25, 8, 12, 5, 2, 19, 1]

numbers_tuple = tuple(numbers_list)

n = int(input("Введіть число n: "))

result = [num for num in numbers_tuple if num < n]

print("Числа з кортежу, які менші за", n, ":", result)
