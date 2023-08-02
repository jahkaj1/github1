# varibles: Objects containing specific values
x=5   #numeric or integer variable
print(x)
y="Ali eating" # string variable
print(y)
x=x+10
print(x)

#types/class of variables
type(x)
print (type (x)) # show type of x but x=15 it means it is integer
print (type(y)) #show type of string because it has ""

#Rules to assign a varible
# 1-The variable should contain letters, numbers and underscores
# 2-Do not start with numbers, for example 2y=2 etc,, it will only start by varibles like x, y etc 
# 3-Spaces are not allowed 
# 4-Do not use keywords in functions forexample(break, mean, media, test etc/) you can check by google "keywords in python".
# 5-Variable names are short and descriptive
# 6-Casesensitivity (Lowercase letters and Uppercase letters)Always use lowercase letters

#Example of variable
fruit_basket="Mangoes, Oranges"  
print(fruit_basket)   #string 

fruit_basket=8         #integer
print(fruit_basket)

fruit_basket=8         #integer
print(type(fruit_basket))   #check type 
print (fruit_basket)

fruit_basket=8         #integer
fruit_basket="Magoes"
print(type(fruit_basket))   #check type 
print (fruit_basket)


fruit_basket=8         #integer
fruit_basket="Magoes"
del fruit_basket         #it will not delete becuae 2 functions are here
print(type(fruit_basket))   #check type 
print (fruit_basket)

fruit_basket=8         #integer
del fruit_basket         #it will not delete becuae 2 functions are here
print(type(fruit_basket))   #check type 
print (fruit_basket)