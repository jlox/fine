from math import sqrt

def calculate_normal( points, i ):
    #get as and bs to calculate the normal
    ax = points[i + 1][0] - points[ i ][0]
    ay = points[i + 1][1] - points[ i ][1]
    az = points[i + 1][2] - points[ i ][2]

    bx = points[i + 2][0] - points[ i ][0]
    by = points[i + 2][1] - points[ i ][1]
    bz = points[i + 2][2] - points[ i ][2]

    normal = [0,0,0]
    normal[0] = ay * bz - az * by
    normal[1] = az * bx - ax * bz
    normal[2] = ax * by - ay * bx

    return normal


def normalize(v):
    magnitude = sqrt(v[0]*v[0]+v[1]*v[1]+v[2]*v[2])
    return [v[0]/magnitude, v[1]/magnitude, v[2]/magnitude]


def dot_product(v0,v1):
    return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2]

def scalar_product(v, c):
    for i in range(len(v)):
        v[i] = v[i] * c
    return v

def add_vectors(v0, v1):
    return [v0[x]+v1[x] for x in xrange(len(v0))]

def sub_vectors(v0, v1):
    return [v0[x]-v1[x] for x in xrange(len(v0))]

def calculate_light(color, point_sources, constants, normal, view):
    iamb = [color[0]*constants[0], color[1]*constants[1], color[2]*constants[2]]
    idiff = [0, 0, 0]
    ispec = [0, 0, 0]

    for light in point_sources:
        l = light[0:3]
        print normal
        print l
        diffuse_light = [light[3]*constants[3]*dot_product(normal, l), light[4]*constants[4]*dot_product(normal, l), light[5]*constants[5]*dot_product(normal, l)]
        idiff = [idiff[0] + (diffuse_light[0] if diffuse_light[0] > 0 else 0), idiff[1] + (diffuse_light[1] if diffuse_light[1] > 0 else 0), idiff[2] + (diffuse_light[2] if diffuse_light[2] > 0 else 0)]
        angle = pow(dot_product(sub_vectors(scalar_product(scalar_product(normal, dot_product(l, normal)), 2), l), view), 2)
        specular_light = [light[3]*constants[6]*angle,light[4]*constants[7]*angle,light[5]*constants[8]*angle]
        ispec = [ispec[0] + (specular_light[0] if specular_light[0] > 0 else 0), ispec[0] + (specular_light[0] if specular_light[0] > 0 else 0), ispec[0] + (specular_light[0] if specular_light[0] > 0 else 0)]

    return [min(255, iamb[x]+idiff[x]+ispec[x]) for x in xrange(3)]
