
def print_triangle(n):
    if n == 0:
        return
    print_triangle(n-1)
    print("*"*n)

def print_opposite_triangles(n):
    if n == 0:
        return
    print("*"*n)
    print_opposite_triangles(n-1)
    print("*"*n)

def print_ruler(n):
    if n == 0:
        return
    print_ruler(n-1)
    print("-"*n)
    print_ruler(n-1)
