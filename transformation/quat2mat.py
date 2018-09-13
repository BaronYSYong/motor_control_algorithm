"""
Reference:
    http://www.euclideanspace.com/maths/geometry/rotations/conversions/quaternionToMatrix/index.htm
"""

import numpy as np
from numpy.linalg import inv

def quaternion2matrix(X,Y,Z,W):
    xx = X * X
    xy = X * Y
    xz = X * Z
    xw = X * W

    yy = Y * Y
    yz = Y * Z
    yw = Y * W

    zz = Z * Z
    zw = Z * W

    m00 = 1 - 2 * ( yy + zz )
    m01 = 2 * ( xy - zw )
    m02 = 2 * ( xz + yw )

    m10 = 2 * ( xy + zw )
    m11 = 1 - 2 * ( xx + zz )
    m12 = 2 * ( yz - xw )

    m20 = 2 * ( xz - yw )
    m21 = 2 * ( yz + xw )
    m22 = 1 - 2 * ( xx + yy )

    m03 = m13 = m23 = m30 = m31 = m32 = 0
    m33 = 1
    
    return np.array([[m00, m01, m02, m03], [m10, m11, m12, m13], [m20, m21, m22, m23], [m30, m31, m32, m33]])

a = quaternion2matrix(0.0491381883621, 0.00858846586198, -0.952004611492, 0.302021145821)

print(a)
print np.dot(a,inv(a))
