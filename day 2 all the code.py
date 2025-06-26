#list

my_list = [1,2,3]
print(my_list)

#list comprehension 

square = [x**2 for x in range (5)]  # expression  for item iterate if condition 
print(square)

#tuples and their immutability 
my_tuple = (1,2,3,"hello")
print(my_tuple)

#immutability in action 
# my_tuple[1] = 10 #it will raise the type error

# dictionary
person = {
    "name" :{
        
    }"maneet",
    "age" : "23"
     
}
print (person["name"])

# nested data structure list
nested_list = [[1,2,3],[4,5]]
print(nested_list)

#nested data structure dic.
nested_dict = {
    "person" : {"name": "maneet ", "age" : "23"}
}
print(nested_dict["person"]["name"])

# sets 
my_sets = [1,2,3]
another_set = set([4,5,6])
empty_set = set()
print(my_sets,another_set,empty_set)

# sets operations 
# 1. adding element 
my_sets = {1,2,3}
my_sets.add(5)
print(my_sets)

# 2. removing element
my_sets.remove(3)

# 3. clear element 
my_sets.clear()

# set operations 
# 1.unioun 
set1 = {1,2,3,4}
set2 = {6,7,8}
unioun_set = set1.union(set2)
print(unioun_set)

intersection_set = set1 & set2
intersection_set = set1.intersection(set2)

#function
# i = {1,2,3,4,5}
# reversed_i =  i[::-1]
# print(reversed_i)

#function 
# 1.positional pqarameter : in which basic pqarameterare passed 
def add(a,b):
    return a+b
print(add(5,3))

#2. default parameter 
def greet(name = "guest"):
    print(f"hello{name} ")
    greet()
    greet("maneet")

def greet(name="guest"):
    print(f"hello{name}")
greet()
greet("manna")
def greet(name = "manna"):
    print(f"hello{name}")
greet()
greet("jass")

# 3. keyword parameter
# def introduce(name,age):
#     print(f"my name is{name}""my age is"{age})
# introduce(age=23,name="maneet" \")

# 4.arbirary argument
# *args:for variable number of positional agrument
def sum_all(*args):
    return sum(args)
print (sum_all(1,2,3,4,5))

def print_details(**kwargs):# kwargs used for defining keyword argument 
    return print(kwargs)
print (print_details(name="manna",age="23"))
        
# return value 
# 1.single return value
def add(a,b):
    return(a+b)
print(add(2,3))

# 2.double return value 
def divide_and_multiply(a,b):
    return(a//b,a*b)
print(divide_and_multiply(2,3))
#3.no return value
def greet():
    print("hello")
result = greet()

# scope of return value --
# 1.local scope: define inside the function
def my_function():
    x=10 #local variable
    print(x)

my_function()



# 2.global variable : define outside the function
x=10
def my_function():
    print(x)       
my_function()

#3.modifying global function:use modify keyword 
x = 10
def modify_global():
    global x
    print(x) 
modify_global()

#4.built in scope:it provide built in function 
print(len([1,2,3]))

# lambda function --
# 1. basic usuage--
add = lambda x,y :x+y
print(add(5,3))
def add():


# 2.mapping in lambda function
numbers =[1,2,3,4]
doubled = list(map(lambda x:x*2,numbers))
print(doubled)

# 3.filter even numbers  in lambda function
numbers =[1,2,3,4]
even = list(filter(lambda x : x % 2 ==0,numbers))
print(even)

# 4. sort nunmber using lambda function
pairs = [(1,2),(3,4),(5,6)]
# sorted_pairs =pairs((lambda x: x[1]))
# print(sorted_pairs)
print(pairs[0])

# Modules 
# 1. creating module 
# a module is python file with.py extension
# my_function.py

# 2. importing modules
import my_module
print(my_module.add(5,3))