import math
import time

print("Triangle area and hypotenuse calculator")
base = int(input("Enter the value of the base: "))
height = int(input("Enter the value of the height: "))
area = 1/2*base*height
hypo = math.sqrt(base**2 + height**2)
time.sleep(1)
print("The area of the triangle is: ",area)
time.sleep(1)
print("The hypotenuse of the triangle is: ", hypo)
print("woohoo! you calculated it!")
