#Generate an inverted right triangle
def inverted_right_triangle(n):

    #for calculating the shape of the triangle
    for i in range(n, 0 , -1):
        print("*" * i)


try:
    #for getting the user input
    height = int(input("Enter the height of the triangle: "))
    #for generating the triangle
    inverted_right_triangle(height)
except ValueError as e:
    print(e)
