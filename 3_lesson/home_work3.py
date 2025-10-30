#1
#1.1
# password = input("Enter password: ")
# if password == 'password123':
#     print("good password")
# else :
#     print("Not correct")
    
#1.2
# day_of_week_int = int(input("Enter day of week: "))
# match day_of_week_int:
#     case 1:
#         day_of_week = 'Monday'
#         print(day_of_week)
#     case 2:
#         day_of_week = 'Tuesday'
#         print(day_of_week)
#     case 3:
#         day_of_week = 'Wednesday'
#         print(day_of_week)
#     case 4:
#         day_of_week = 'Thursday'
#         print(day_of_week)
#     case 5:
#         day_of_week = 'Friday'
#         print(day_of_week)
#     case 6:
#         day_of_week = 'Saturday'
#         print(day_of_week)
#     case 7:
#         day_of_week = 'Sunday'
#         print(day_of_week)
#     case _:
#         print("Not correct number")


#2
#2.1
# numb = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(numb," * ",i," = ", numb*i)
#     i+=1

#2.2
# arr = [1,2,4,6,7]
# sum=0
# for value in arr:
#     sum += value
# print(sum)

#2.3
# num_of_fact = int(input("Enter num for factorial: "))
# fact = 1
# i=1
# if num_of_fact == 0:
#     print(num_of_fact,"! = 1")
# elif num_of_fact > 0: 
#     while i<=num_of_fact:
#         fact*=i
#         i+=1
#     print(num_of_fact,"! = ", fact)
# else :
#     print("Not correct number")

#2.4
# i=1
# while i<=50:
#     if i% 2 == 0:
#         print(i)
#     i+=1

#2.5
left_limit = int(input("Enter left limit: "))
right_limit = int(input("Enter right limit: "))
while left_limit<=right_limit:
    i = 2
    check= True
    while  i < left_limit:
        if left_limit % i ==0:
            check = False
            break
        i+=1
    if left_limit == 1 or left_limit == 0:
        check = False
    if   check :
        print(left_limit)
    left_limit +=1