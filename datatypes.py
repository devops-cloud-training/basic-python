print("Hello Sathish")

# Numbers
# Lists
# Tuples
# Strings
# Set
# Dict

print("====================================================")
a = 10
print(a)
print(type(a))

b=10.5
print(b)
print(type(b))

x = a+int(b)
print(x)
print(type(x))

c=4+2j
print(c)
print(type(c))

# List datatype
print("====================================================")
rank = [1,2,3,4,5,6,7,1,2,3,4,5,6,7]
food = ["biriyani","kesari","rice"]

print(rank[::-1])

food.append("idly")
food.insert(0,"dosa")

rank.extend(food)

rank.remove("biriyani")

del food[2]

mixes = [1,2,3,"abc","def"]

print(rank)
print(mixes)
print(type(mixes))
print(food)
print(rank[-5:-2])
print(len(rank))
print(rank.count(2))
print(rank.count(3))

# tuples datatype

rank = (1,2,3,4,5,6,7,4,3,4,56,6,54,3,3,3,2,1,2,3,4,5,6,7)
food = ("biriyani","kesari","rice")
mixes = (1,2,3,"abc","def")

print(rank)
print(mixes)
print(type(mixes))
print(food[1])


# Strings
print("====================================================")

name = "Sathish"
print(name)
print(type(name))
print(name[3])

message = """
hello guys
how are you
where are you
"""

print(message)

employee="asdfkRETRTlajhsdklfjaklsjdf"

print(employee[1:5])
print(employee[::-1])

print(employee.isupper())

# Set datatype
print("====================================================")

rank = {1,2,3,4,5,6,7,1,2,3,4,5,6,7}
food = {4,6,"biriyani","kesari","rice","kesari","biriyani","biriyani","biriyani"}
print(rank)
print(type(rank))
print(food)
# rank = {5}
union_set=rank.union(food)
another_union_set = rank|food
print(union_set)
print(another_union_set)

intersection_set=rank.intersection(food)
another_intersection_set = rank&food
print(intersection_set)
print(another_intersection_set)

difference_set=rank.difference(food)
another_difference_set = rank-food
print(difference_set)
print(another_difference_set)

# Dictionary datatype
print("====================================================")

employee_data = {
    "name": "Sathish",
    "state": "tn",
    "salary": 908908098209809,
    "domain": "cloud"
}

print(employee_data["name"])
print(type(employee_data))
