import numpy as np

def get_barycentric_coordinates(triangle_coordinates:np.ndarray, point_coordinates:np.ndarray) -> np.ndarray:
    """Returns the barycentric coordinates of a cartesian point (x,y) with
    respect to a triangle with vertices (x1,y1), (x2,y2), (x3,y3)"""
    barycentric_point = np.linalg.solve(triangle_coordinates, point_coordinates)
    return np.asarray(barycentric_point)

def get_cartesian_coordinates(triangle_coordinates:np.ndarray, barycentric_coordinates:np.ndarray) -> np.ndarray:
    """Returns the cartesian coordinates (x,y) of a point in barycentric coordinates
    with respect to a triangle with vertices (x1,y1), (x2,y2), (x3,y3)"""
    fixed_vector = np.transpose(barycentric_coordinates) #changes to appropriate dimensions
    cartesian_point = np.matmul(triangle_coordinates, fixed_vector) #matrix-vector mult
    return cartesian_point

def is_inside_triangle(triangle_coordinates:np.ndarray, point_coordinates:np.ndarray) -> bool:
    """Determines whether a point (x,y) is inside a triangles with vertices
     (x1,y1), (x2,y2), (x3,y3)"""
    barycentric_point = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    if np.all(barycentric_point >=0):
        return True
    else:
        return False