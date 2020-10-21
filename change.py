import math

class Quaternion:
    w = 0
    x = 0
    y = 0
    z = 0

class EulerAngles:
    roll = 0
    pitch = 0
    yaw = 0


q = Quaternion()
q.x = 0
q.y = 0
q.z =  0.652192565502

q.w = 0.758053334208

angles = EulerAngles()

# sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
# cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
# angles.roll = math.atan2(sinr_cosp, cosr_cosp)

# // pitch (y-axis rotation)
# sinp = 2 * (q.w * q.y - q.z * q.x)
# if (abs(sinp) >= 1)
#     angles.pitch = std::copysign(M_PI / 2, sinp); // use 90 degrees if out of range
# else
#     angles.pitch = std::asin(sinp)

siny_cosp = 2 * (q.w * q.z + q.x * q.y)
cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
angles.yaw = (math.atan2(siny_cosp, cosy_cosp))*(180/math.pi)
 
print(angles.yaw)
