# 40. Varibel Scope = The visibility of a variable in a program
# Scope resolution = (LEGB) Local, Enclosing, Global, Built-in

# Local = Variable defined inside a function
def func1 ():
    x = 10
    print(x)

# Enclosing = Variable defined in the local scope of a function, but not in the global scope
def func2 ():
    x = 10
    def func3 ():
        print(x)
    func3()

# Global = Variable defined in the global scope
x = 10

def func3 ():
    print(x)
# Built-in = Variable defined in the built-in scope

