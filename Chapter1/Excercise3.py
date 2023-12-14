# The function definition to check the validity .
def is_valid_triangle(sideA, sideB, sideC):
    if sideA + sideB>= sideC and sideB + sideC>= sideA and sideC + sideA>= sideB:
        return True
    else:
        return False
    
# The tree sides of a Triangle.
sideA = float(input('Ener the length of sideA:'))
sideB = float(input('Ener the length of sideB:'))
sideC = float(input('Ener the length of sideC:'))

# The function & making
if is_valid_triangle(sideA, sideB, sideC):
    print('triangle is valid.')
else:
    print('triangle is invalid.')