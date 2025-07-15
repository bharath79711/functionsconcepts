"""
def name(s):
    return s

x=name(input("enter your name:"))
print("Hello !",x)



y=name(int(input("enter your age:")))
print("age is:",y)
"""
"""
name = input("Enter your name: ")
age = int(input("Enter your age:"))

print("Hello",name,"love u")
print("You are",age ,"years old")

"""
"""
age =int(input("Enter your age:"))
if age >=18:
    print("your eligible for vote Doctor.")
else:
    print("your not eligible to vote Doctor.")
"""
"""
marks=int(input("Enter your marks Doctor."))
if marks >=90:
    print("your Grade: A+")
elif marks >=75:
    print("your Grade:A")
elif marks>=60:
    print("your Grade:B")
else:
    print("your Grade:C")
"""
"""
number = int(input("Enter a number:"))
if number%2==0:
    print(number,":is even",int(number/2))
else:
    print(number,"is odd number.")
"""

"""
for i in range(1,6):
    print("love you Doctor")

count=1
while count<=5:
    print("love you Doctor",count)
    count=count+1
"""
"""
y=[]
for i in range(1,11):
    y.append(i)
print(y)
"""
"""
count=1
odd_count=0
y=[]
while odd_count < 5:
    y.append(count)
    count=count+2
    odd_count=odd_count+1
print(y)

"""
"""

def greet(name):
    print("hello",name)

greet("Doctor")


def add(x,y):
    z= x+y
    return z


xx=add(10,20)
print(xx)


def sq_num(num):
    return num*num


A=sq_num(10)
print(A)



def is_even(n):
    if n % 2==0:
        return "even"
    else:
        return "odd"

B=is_even(12)
print("is",B)
C=is_even(13)
print("is odd",C)
"""
"""
fruits=["apple","Banana","Mango"]
print(fruits[0])
fruits.append("orange")
print(fruits)


colors = ("Red","Green","Yellow")
print(colors[1])

nums ={1,2,2,3,4,5,5,6,6,7}
print(set(nums))



student_det ={"name":"Bharath",
              "Age":28,
              "School":"Zphs",
              "Pin_code":516172}
print(student_det["name"])
student_det["Age"]=29
student_det["Branch"]="Mech"
print(student_det)


places =["Hyderabad","Bangalore","chennai","pune","Delhi"]
print(places[3])
print(places[-1])


colors_new =("white","Black","Orange","pinck")
print(colors_new[2])

unique_num ={9,9,9,8,8,7,7,6,5,4,3,3,2,2,1}
print(set(unique_num))


dic_deta = {"name":"Doctor","Age":25,"food":"chicken"}
print(dic_deta["name"])
dic_deta["Age"]=29
dic_deta["Nature"]="so sweet"
print(dic_deta)
for keys,values in dic_deta.items():
    print(values)
"""

"""
start =int(input("Enter a start number:"))
End  = int(input("Enter a end number"))
even_count=0
odd_count=0
for i in range(start,End+1):
    if i%2==0:
        even_count=even_count+1

    else:
        odd_count=odd_count+1

print("Even numbers count:",even_count)
print("odd numbers count:",odd_count)

"""
"""
sentence = input("Enter a sentence: ")
vowel_count=0
vowels="aeiouAEIOU"
for char in sentence:
    if char in vowels:
        vowel_count=vowel_count+1
print("How many vowels in sentence:",vowel_count)

"""

"""

word = input("Enter a word:")

if word ==word[::-1]:
    print("it's a palindrome.")
else:
    print("it's not a palindrome.")

"""




"""
sentence = input("Enter a sentence:")

x={}
for char in sentence:
    if char.islower():
        if char in x:
            x[char]=x[char]+1
        else:
            x[char]=1

print(x)
"""

"""
for keys,values in x.items():
   print(keys,values)
"""

"""
sentence=input("Enter a sentence:").lower()
words=sentence.split()
word_count={}

for word in words:

    if  word in word_count:
        word_count[word]=word_count[word]+1
    else:
        word_count[word]=1

print(word_count)

"""

























