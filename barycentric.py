import numpy as np

def get_barycentric_coordinates(triangle_coordinates:np.ndarray, point_coordinates:np.ndarray) -> np.ndarray:
    """Returns the barycentric coordinates of a cartesian point (x,y) with
    respect to a triangle with vertices (x1,y1), (x2,y2), (x3,y3)"""
    triangle_coordinates = np.asarray(triangle_coordinates)
    if triangle_coordinates.shape != (2,3):
        return print("Make sure the matrix of triangle vertices is 2x3")

    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]

    x,y = point_coordinates

    triangle_array = np.array([[x1 - x3, x2 - x3], [y1 - y3, y2- y3]])             #here we use the third vertex as a reference
    point_array = np.array([x-x3, y-y3])        #these set up the system to be used in np.linalg.solve

    lambda1, lambda2 = np.linalg.solve(triangle_array, point_array) #returns scalar coefficients that solve system
    lambda3 = 1 - (lambda1 + lambda2)               #solves for lambda3 in terms of lambda1, lambda2

    return np.array([lambda1, lambda2, lambda3])

def get_cartesian_coordinates(triangle_coordinates:np.ndarray, barycentric_coordinates:np.ndarray) -> np.ndarray:
    """Returns the cartesian coordinates (x,y) of a point in barycentric coordinates
    with respect to a triangle with vertices (x1,y1), (x2,y2), (x3,y3)"""

    fixed_vector = np.transpose(barycentric_coordinates) #changes to appropriate dimensions
    cartesian_point = np.matmul(triangle_coordinates, fixed_vector) #matrix-vector mult gives us the change of coordinates

    return cartesian_point

def is_inside_triangle(triangle_coordinates:np.ndarray, point_coordinates:np.ndarray) -> bool:
    """Determines whether a point (x,y) is inside a triangles with vertices
     (x1,y1), (x2,y2), (x3,y3)"""

    barycentric_point = get_barycentric_coordinates(triangle_coordinates, point_coordinates)

    if np.all(barycentric_point >=0): #checks if all 3 points are non-negative
        return True
    else:
        return False
