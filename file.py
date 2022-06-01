num1 = 42 #variable declaration - number #
num2 = 2.3  #variable declaration - number #
boolean = True  #v.d. - boolean #
string = 'Hello World' #v.d. - string#
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #v.d - list - initialize#
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #v.d. - Dictionary - Initialize#
fruit = ('blueberry', 'strawberry', 'banana') #v.d. - tupla - initialize#
print(type(fruit)) #log statement - type check - tuple - access value#
print(pizza_toppings[1]) #log statement - list - access value#
pizza_toppings.append('Mushrooms') #list - add value#
print(person['name'])#log statement - dictionary - access value#
person['name'] = 'George'   #dictionary - change value#
person['eye_color'] = 'blue'    #dictionary - add value#
print(fruit[2]) #log statement - tuple - access value#

if num1 > 45: #if
    print("It's greater")#log statement - string
else: #else
    print("It's lower") #log statemnt - string

if len(string) < 5: #if - length check - string#
    print("It's a short word!") #log statement - string
elif len(string) > 15: #else if - length check - string#
    print("It's a long word!") #log statement - string
else: #else
    print("Just right!") #log statement - string

for x in range(5): #for sequence
    print(x) #log statement - number
for x in range(2,5): #for sequence
    print(x) #log statement - number
for x in range(2,10,3): #for sequence
    print(x) #log statement - number
x = 0 #variable declaration - number
while(x < 5): #while - stop
    print(x) #variable declaration - number
    x += 1 #while - increment - number

pizza_toppings.pop() #list - delete value
pizza_toppings.pop(1) #list - delete value

print(person) #log statement - dictionary - access value
person.pop('eye_color') #dictionary - delete value
print(person) #log statement - dictionary - access value

for topping in pizza_toppings: #for start -list - access value
    if topping == 'Pepperoni': #if string
        continue # for continue
    print('After 1st if statement') #log statement - string
    if topping == 'Olives': # if string
        break # for break

def print_hello_ten_times(): #function
    for num in range(10): #for start - number
        print('Hello') #log statement - string

print_hello_ten_times() #function 

def print_hello_x_times(x): #function parameter
    for num in range(x): #for start - number
        print('Hello') #log statement - string

print_hello_x_times(4) #function - argument - number

def print_hello_x_or_ten_times(x = 10): #function parameter - argument - number - variable declaration
    for num in range(x): #for start - number
        print('Hello') #log statement - string

print_hello_x_or_ten_times()#function 
print_hello_x_or_ten_times(4)#function argument


"""
Bonus section
"""

# print(num3) NameError: name <num3> is not defined
# num3 = 72 
# fruit[0] = 'cranberry' TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) KeyError: 'favorite_team'
# print(pizza_toppings[7]) IndexError: list index out of range
#   print(boolean) name <boolean> is not defined
# fruit.append('raspberry') AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) AttributeError: 'tuple' object has no attribute 'pop'