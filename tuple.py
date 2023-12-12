#Program to print a pattern of asterisks in the form of a right-angled triangle.
'''
def print_triangle(n):
    for i in range(1,n+1):
        print('* ' * i)
        
n = 5
print_triangle(n)
'''


#inverted triangle
def inverted_triangle_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(0, i):
            print("*", end=' ')
        print("\n")

inverted_triangle_pattern(5)


#Nested Form
def inverted_triangle_pattern(rows):
    for i in range(rows, 0, -1):
        for j in range(0, rows - i):
            print(" ", end=' ')
        for k in range(0, i):
            print("*", end=' ')
        print("\n")

inverted_triangle_pattern(5)


