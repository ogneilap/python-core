#1
#1.1
test_list = [12,31,23,33,22]
print(test_list)
test_list.append(10)
test_list.append(20)
test_list.remove(10)
print(test_list)

#1.2
copy_list = test_list.copy()
print(copy_list)
t_sum = 0
for element in copy_list:
    t_sum += element
print(t_sum)

#1.3
print(copy_list)
for i in range(len(copy_list)):
    copy_list[i] *=2
print(copy_list)


#2
#2.1
fruits = ('banana','apple', 'orange')
for fruit in fruits:
    print(fruit)
    
#2.2
kort_first = (1,2,3,5,4)
kort_second = (10,11,23,23,12)
kort_Update = kort_first + kort_second
print(kort_first)
print(kort_second)
print(kort_Update)


#3
#3.1
sport_man = {'name': 'Stas', 'age': 18,'sport': 'footbal','camand': 'Popivska' }
print(sport_man)

#3.2
book = {
    'Garri Potter': 1945,
    'Pid kypolom':1978}
print(book)
book['abetka'] = 1232
print(book)

#3.3

contry_capital = {
    'Ukrain': 'Kyiv',
    'Poland': 'Vbarhava',
    'German': 'Berlin'}
print(contry_capital)
print(contry_capital.get('Ukrain',"dont have"))
print(contry_capital.get('USA','dont have'))