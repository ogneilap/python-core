#1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
#2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

def calculate_average(numbers):
    avarage = 0
    for i in numbers:
        avarage += i
    avarage /= len(numbers)
    return avarage

def find_max(numbers):
    max_numb = numbers[0]
    for i in numbers:
        if i> max_numb:
            max_numb = i
    return max_numb
    
