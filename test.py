
import numpy as np
from scipy.optimize import fsolve, root, leastsq
from data import coordinate_carla, coordinate_real
import math
 
# 定义方程组
# parameters[0] = theta,  
# parameters[1] = X'
# parameters[2] = Y'



# coordinate_carla = [[1175.3355712890625, -193.1874237060547],
#                     [1048.436767578125, -116.30294799804688],
#                     [1227.86474609375, -70.40817260742188]]

# coordinate_real = [[35.7604675293, 102.364402771],
#                    [-75.1433181763, 206.356018066],
#                    [-66.2030334473, 60.5677452087]]
            


# for index in range(len(coordinate_carla)):
#     if index != len(coordinate_carla)-1:
#         dis = ((coordinate_carla[index][0] - coordinate_carla[index+1][0])**2 +\
#                 (coordinate_carla[index][1] - coordinate_carla[index+1][1])**2)**0.5
#         print("coordinate_carla:", dis)

#         dis = ((coordinate_real[index][0] - coordinate_real[index+1][0])**2 +\
#                 (coordinate_real[index][1] - coordinate_real[index+1][1])**2)**0.5
#         print("coordinate_real:", dis)

#     else:
#         dis = ((coordinate_carla[index][0] - coordinate_carla[0][0])**2 +\
#                 (coordinate_carla[index][1] - coordinate_carla[0][1])**2)**0.5
#         print("coordinate_carla:", dis)
#         dis = ((coordinate_real[index][0] - coordinate_real[0][0])**2 +\
#                 (coordinate_real[index][1] - coordinate_real[0][1])**2)**0.5
#         print("coordinate_real:", dis)

def func(parameters):
    linear_equation = []
    for index in range(len(coordinate_carla)):
        linear_equation.append(math.cos(parameters[0])*coordinate_real[index][0] +
                               math.sin(parameters[0])*coordinate_real[index][1] +
                               parameters[1] - coordinate_carla[index][0])
        linear_equation.append(-math.sin(parameters[0])*coordinate_real[index][0] +
                               math.cos(parameters[0])*coordinate_real[index][1] +
                               parameters[2] - coordinate_carla[index][1])

    # a = [x[0] * np.cos(x[1]) - input[0],
    #         x[1] * x[0] - x[1] - input[1]]
    return linear_equation

def check_func(ans):
        for index in range(len(coordinate_carla)):
                x_carla_cal = math.cos(ans[0][0])*coordinate_real[index][0] + \
                                math.sin(ans[0][0])*coordinate_real[index][1] + \
                                ans[0][1] - coordinate_carla[index][0]
                y_carla_cal = -math.sin(ans[0][0])*coordinate_real[index][0] + \
                                math.cos(ans[0][0])*coordinate_real[index][1] + \
                                ans[0][2] - coordinate_carla[index][1]
                print("coordinate_error:", x_carla_cal, y_carla_cal)

def func_new(parameters):
    linear_equation = []
    for index in range(len(coordinate_carla)-3):
        index = index + 3
        linear_equation.append(parameters[0]*coordinate_real[index][0] +
                               parameters[1]*coordinate_real[index][1] +
                               parameters[2] - coordinate_carla[index][0])
        linear_equation.append(parameters[3]*coordinate_real[index][0] +
                               parameters[4]*coordinate_real[index][1] +
                               parameters[5] - coordinate_carla[index][1])

    # a = [x[0] * np.cos(x[1]) - input[0],
    #         x[1] * x[0] - x[1] - input[1]]
    return linear_equation

def check_func_new(parameters):
        for index in range(len(coordinate_carla)):
                x_carla_cal = parameters[0]*coordinate_real[index][0] + \
                        parameters[1] * coordinate_real[index][1] + \
                        parameters[2] - coordinate_carla[index][0]
                y_carla_cal = parameters[3]*coordinate_real[index][0] + \
                        parameters[4] * coordinate_real[index][1] + \
                        parameters[5] - coordinate_carla[index][1]
                print("coordinate_error:", x_carla_cal, y_carla_cal)

# for i in range(36):
#     print(i*10)
ans = leastsq(func_new, [0, 0, 0, 0, 0, 0])

# ans_root = root(func_new, [0, 0, 0, 0, 0, 0], method='lm')

print(ans[0])  
# print(ans_root['x']) 

check_func_new(ans[0])
# print(ans[0][0])

# print(np.isclose(func(ans[0]), [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]))
# check the ans

