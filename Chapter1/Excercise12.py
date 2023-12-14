#Create a avariable that differs the choices
choice=int(input("What do you want to calculate:\n 1.Triangle \n 2.Rectangle \n 3.Circle"))
if choice==1:
    choice2=int(input("What do you want to calculate with: \n 1. area \n  2. Perimeter"))
    if choice==2:
        base=float(input("enter the base = "))
        height=float(input("enter the height ="))
        area= 0.5*base*height
        print("The area of the Rectangle is", area)

    elif choice2==2:
        s1=float(input("enter the side1 = "))
        s2=float(input("enter the side2 = "))
        s3=float(input("enter the side3 = "))
        peri = s1+s2+s3
        print("the area of the triangle is", peri)
elif choice==2:
    choice2=int(input("what do you want to calculaate with: \n 1.area \n 2.perimeter"))
    if choice2==1:
        s=float(input("enter the sides ="))
        area=4*s
        print("the area of the square is", area)

else:
    print("invalid")