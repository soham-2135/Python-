#1)
def calculate_area(base,height):
    return 1/2* base*height

area=calculate_area(4,5)
print("Area of traingle is",area)

def calculate_area1(length,width):
    return length*width

area_1=calculate_area1(4,5)
print("Area of rectangle is",area_1)

#we created two seperate functions for calculating area of triangle in the above code

# 1) Write a function called calculate_area that takes base and height as an input
# and returns and area of a triangle. Equation of an area of a triangle is,
#  area = (1/2)*base*height

# 2) Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(dimension1,dimension2,shape="triangle"):
    if shape=="triangle":
        area=1/2*(dimension1*dimension2)
    elif shape=="rectangle":
        area=dimension1*dimension2
    else:
        print("Error: input shape is neither rectangle nor triangle")
        area= None #here we have specified area as none, without it we cant called return area below, so its necessary
    return area

#i)
triangle_area=calculate_area(4,5,"triangle")
print(f"Area of triangle is {triangle_area}")

#another way
base=5
height=10
triangle_area=calculate_area(base,height,"triangle")
print(f"Area of triangle is {triangle_area}")

#ii)
rectangle_area=calculate_area(4,5,"rectangle")
print(f"Area of rectangle is {rectangle_area}")

#another way
height=5
width=10
rectangle_area=calculate_area(height,width,"rectangle")
print(f"Area of triangle is {rectangle_area}")

#iii)trying default parameter
base=5
height=10
triangle_area=calculate_area(base,height)
print(f"Area of triangle is {triangle_area}")

#iv)Trying else condition
square_area=calculate_area(5,10,"square")
print(f"Area of square is {square_area}")

# 3. Write a function called print_pattern that takes integer number as an argument
# and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(input_value=5):
    for i in range(input_value):
        s=''
        for j in range(i+1):
            s = s+'*'
        print(s)

print("\npattern for input 3 is:")
print_pattern(3)
print("\npattern for input 4 is:")
print_pattern(4)
print("\npattern for default input is:")
print_pattern()
