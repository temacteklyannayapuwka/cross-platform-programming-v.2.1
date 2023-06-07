import math

print("Write your numbers")
a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

p = ((a + b + c) / 2)
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print("Right answer: ",s)
input('Press ENTER to exit')