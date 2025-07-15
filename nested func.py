"""
def greet():
    print("Hi Bharath")

    def message():
        print("your learning nested functions perfectly")

    message()

greet()

"""
"""
def name(name):
    def inner():
        print(f"Hello {name},you're my favorite student")
    inner()

name("Bharath")
"""
"""
def welcome(name):
    def message():
        return (f"{name} ,Welcome to the python nested functions.")

    return message()
data=welcome("Bharath")
print(data)
"""

"""
def multiply(x):
    def inner():
        return x*2
    return inner()

y=multiply(10)
print(y)

z=multiply(12)
print(z)
"""

"""
def outer_func(a,b):
    def add():
        return a+b
    def multiply():
        return a*b
    return  add(),multiply()


sum_result , product_result =outer_func(10,15)

print("Sum_result:",sum_result)
print("product_result:",product_result)

"""
"""
def power_func(n):
    def power(x):
        return x ** n
    return power

square=power_func(2)
cube=power_func(3)
print("Square of 5:",square(5))
print("cube of 3:",cube(3))

"""
"""
def calculator(a,b):
    def add():
        return a+b
    def substract():
        return a-b
    def multiply():
        return a*b
    def division():
        if b!=0:
            return a/b
        else:
           return "Division by zero is not allowed"
        
    return add(),substract(),multiply(),division()
add_res,sub_res,mult_res,div_res = calculator(5,0)

print("Add:",add_res)
print("substraction:",sub_res)
print("multiply:",mult_res)
print("Divsion:",div_res)
"""

"""
def name(s1,s2):
    def format_name():
        return s2 +s1.title()
    return format_name()


print(name("Bharath kumar", " Talari"))
"""
"""
def convert(temp):
    def celsius():
        return (temp-32)* 5/9
    def fahernheit():
        return (temp*9/5)+32
    return celsius(),fahernheit()


cel_res,fah_resu = convert(100)


print("celsius:",cel_res)
print("fahernheit:",fah_resu)

"""

"""
def sq_cub(num):
    def sq():
        return num ** 2
    def cub():
        return num** 3
    return sq(),cub()

sq_res,cub_res =sq_cub(5)


print("square of 5:",sq_res)
print("cube of 5:",cub_res)

"""
"""
def my_name(func):
    def inner_age(name,age):
        if age>=18:
            return func(name,age)
        else:
            return "please check age is greater than 18."
    return inner_age




def name(name,age):
    return (f"Hello {name} you're Eligible to vote.")

dec_func=my_name(name)

x=dec_func("Bharath",19)
print(x)


#data=name('Bharath',15)
#print(data)

"""

"""
def Running_func(func):
    def inner(a,b):
        print("Running function...")
        result=func(a,b)
        print("result:",result)
        print("Function finished....")
        return result
    return inner



@Running_func
def add(a,b):
    return a+b

@Running_func
def multiply(a,b):
    return a*b


add(10,20)

multiply(15,10)

"""


"""
def Running_func(func):
    def inner(a,b):
        print("Running function...")
        result=func(a,b)
        print("result:",result)
        print("Function finished....")
        return result
    return inner




def add(a,b):
    return a+b


def multiply(a,b):
    return a*b


x=Running_func(add)

y=x(10,5)
z=x(10,10)
"""

"""
def log(func):
    def inner(n):
        print(f"[log] you passed a number:{n}")
        return func(n)
    return inner



#@log
def calculate(n):
    def sq():
        return n**2
    def cub():
        return n**3
    return sq(),cub()

sq_res,cub_res=calculate(5)
print("sq:",sq_res)
print("cub:",cub_res)
decr_func=log(calculate)
x=decr_func(5)
print(x)

"""


"""

def valid_inputs(func):
    def inner(a,b):
        if a <0 or b<0:
            return "only possitive numbers allowed"
        elif b == 0:
             return "plese avoid zero in place of b "
        elif b>a:
            a,b = b,a
            return func(a,b)
        else:
            return func(a,b)
    return inner



#@valid_inputs
def div(a,b):
    return a/b


print(div(12,4))
print(div(4,12))
print(div(10,0))


dec_re=valid_inputs(div)
x=dec_re(24,2)
print(x)
re=valid_inputs(div)
y=re(2,10)
print(y)
"""
"""
def my_val(func):
    def inner(a,b):
        if a % 2==0 and b % 2==0:
            print("a and b are even numbers square the both values.")
            return a**2,b**2
        else:
            return a**3 ,b**3
    return inner

@my_val
def sq_cub(a,b):
    pass




print(sq_cub(2,4))
print(sq_cub(3,7))
print(sq_cub(9,4))

"""
"""
def logger_func(func):
    def inner(*arg,**kwargs):
        used_args= args if args else kwargs
        print("calling function with:", used_args)
        result=func(*args,**kwargs)
        print("result:",result)
        return result
    return inner

@logger_func
def add(a,b):
    return a+b

print(add(10,20))
"""

"""
def possitive_only(func):
    def inner(a,b):
        if a > 0 and b > 0:
            return func(a,b)
        else:
            return "only possitive numbers are allowed.!"
    return  inner


def multiply(a,b):
    return a*b

dec_possitive=possitive_only(multiply)
x= dec_possitive(10,20)
print("prodct of a and b:",x)
y=dec_possitive(-10,20)
print(y)

"""

try:
    a=int(input("Enter a number of a:"))
    b=int(input("Enter a number of b:"))
    result=(a/b)
    raise Exception("error found")
except Exception as error:
    print("error is:",error)
else:
    print("Division is succesful! Result is :",result)
finally:
    print("this program will be Done clearly")






























