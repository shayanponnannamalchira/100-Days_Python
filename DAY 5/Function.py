def greet():
    print("Hello, World!")
    
greet()

def add(a,b):
    return a+b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("sum =",add(a,b))

def greet(name="Guest"):
    print(f"Hello, {name}!")
    
greet("Alice")