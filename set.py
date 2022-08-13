my_set = {1,2,3,4,5,1}
print(my_set)

my_list = [1,2,3,4,5,1]
print(set(my_list))

(my_set.add(10))
print(my_set)

print( 10 in my_set)

# Set Methods
set_one = {1,2,3,4,5}
set_two ={4,5,6,7,1}

print ( set_one.difference(set_two))  # Find Difference 

set_one.discard(5) #Discard Data 
print(set_one)

print(set_one.intersection(set_two))  # Intersection of Two Sets # or  print ( set_one & set_two)

set_one.difference_update(set_two) # Discuard Data From One Set that is Available in Another Set
print(set_one)

print(set_one.isdisjoint(set_two))  # Check If Two sets have something not common;

set_one.union(set_two) # or  print ( set_one | set_two)
print(set_one)


# super set or sub set

my_set_one = {1,2}
my_set_two ={1,2,3,4,56,7,8,9}
print(my_set_one.issubset(my_set_two))
print(my_set_one.issuperset(my_set_two))