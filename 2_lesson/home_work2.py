#1
# 1.1
print("1.1-----------------")
num_str = 125
print(type(num_str),num_str)
num_str = str(num_str)
print(type(num_str),num_str)

#1.2
print("1.2-----------------")
massage = 'Hi my name is Python!'
print(massage)
massage = massage.replace('y', 'o').replace('i', '1')
print(massage)

#1.3
print("1.3-----------------")
split_test ='This is a split test'
print(split_test)
split_test = split_test.split()
print(split_test)
split_test = " ".join(split_test)
print(split_test)

#1.4
print("1.4-----------------")
string_join = 'I am y shokax'
print(len(string_join), " ", string_join)
  
  
#2
#2.1
print("2.1-----------------")
list_append = [1,2,3]
print(list_append)
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

#2.2
print("2.2-----------------")
list_extend =[4,5,6]
print(list_extend)
list_extend.extend([7,8,9])
print(list_extend)

#2.3
print("2.3-----------------")
print(list_extend.index(6))

#2.3
print("2.3-----------------")
print(len(list_extend))


#3
#3.1
print("3.1-----------------")
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'],dict_test['where'])

#3.2
print("3.2-----------------")
print(dict_test.keys(), dict_test.values())

#3.3
print("3.3-----------------")
print(dict_test.items())