#creating strings
Greeting="Hello"
Name="John"

#string connection/concatenation
Introduction=Greeting+","+Name+"!"
print(Introduction)

#repeating strings
laugh="ha"*3
print(laugh)

#accesing characters in a string
print(Name[2])  #prints the third character

#string slicing
print(Name[1:4])  #prints characters from index 1 to 3

# String methods examples
print(Name.lower())   
print(Name.upper())   
print(Name.isalpha()) # True (checks if all chars are alphabets)
print(Name.replace("J", "E"))  