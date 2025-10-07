# Predict the output and try changing variable names
x=50
def func():
    x=100
    print("Inside Function", x)

func()
print("Outside Function", x)

# Global keyword example
count=0

def increment():
    global count
    count+=1
    
increment()
print(count)