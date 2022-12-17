import numpy as np
import random

""" 
создание масива(матрицы) три на три при помощи модуля numpy и заполненнго случайными числами от 0 до 10
транспонирования матрицы 

"""


matrix_a = np.random.randint(0, 10, (3, 3))
print(matrix_a)

matrix_a_T= np.transpose(matrix_a)
print(matrix_a_T)