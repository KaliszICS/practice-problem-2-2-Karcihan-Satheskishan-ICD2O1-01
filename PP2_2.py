'''
    Lesson: If and Else
    Author: Karcihan Satheskishan
    Date Created: October 15, 2024
    Date Last Modified: October 16, 2024
'''
def q1(): 
  num = int(input("Input an integer: "))
  if num == 5:
    print("The number is Five")
  else:
    print("The number is not Five")

def q2(): 
  num=int(input("Enter a number: "))
  if num > 0:
    print("Positive")
  else:
    print("Negative")

def q3(): 
  num=int(input('Input an integer: '))
  if num%2 == 0:
    print("Even")
  else:
    print("Odd")

def q4(): 
  word=input('Type "Hello": ')
  if word=="Hello":
    print('The word is "Hello"')
  else:
    print('The word is not "Hello"')


#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()
#q4()