#Dictionary

dictionary ={
    'a':1,
    'b':2
}
print(dictionary)
print(dictionary.get('c'))

print('a' in dictionary)
print('d' in dictionary)
print(1 in dictionary.keys())
print(1 in dictionary.values())
print(dictionary.items())
dictionary.pop('b')
print(dictionary)
(dictionary.update({'a' : 55}))
print(dictionary)


user_2 = dict(name= "Work")
print(user_2)
user_2.clear()
print(user_2)
# my_list =[
#     {
#         'a' :[1,2,3],
#         'b':True
#     },
#     {
#         'a' :[4,5,6],
#         'b':False
#     }
# ]
# print(my_list[0]['a'][2])