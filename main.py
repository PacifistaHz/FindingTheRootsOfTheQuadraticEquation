import math

a=input("Enter the a's value: ")
b=input("Enter the b's value: ")
c=input("Enter the c's value: ")
a=int(a)
b=int(b)
c=int(c)

discriminant=math.pow(b,2)-4*a*c

if discriminant<0:
    print("No root of quadratic equation.")
elif (discriminant==0):
    print("Have a reel root of quadratic equation.")
    root1=root2=(-b)/(2*a)
    print("The root= "+str(root1)+".")
else:
    print("Have two reel roots of quadratic equation.")
    root1=(-b + math.sqrt(discriminant))/(2*a)
    root2=(-b - math.sqrt(discriminant))/(2*a)
    print("The first root= "+str(root1)+".")
    print("The second root= "+str(root2)+".")