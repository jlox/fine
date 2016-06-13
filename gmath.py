from math import sqrt
def calculate_normal( ax, ay, az, bx, by, bz ):
    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx
    return normal

def calculate_dot( points, i ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[i + 2][0] - points[ i ][0]
    by = points[i + 2][1] - points[ i ][1]
    bz = points[i + 2][2] - points[ i ][2]

    normal = calculate_normal( ax, ay, az, bx, by, bz )

    #set up the view vector values
    vx = 0
    vy = 0
    vz = -1
    
    #calculate the dot product
    dot = normal[0] * vx + normal[1] * vy + normal[2] * vz
    
    return dot

def normalize(v):
    magnitude = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    return [v[0]/magnitude, v[1]/magnitude, v[2]/magnitude]


def dot_product(v0,v1):
    return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

def scalar_product(v, c):
    for i in range(len(v)):
        v[i] = v[i] * c


