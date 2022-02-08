import numpy as np
from sympy import *


class TwoVariablesMinimization:
    def __init__(self, first_value, first_degree, second_value, second_degree):
        self.first_value = first_value
        self.first_degree = first_degree
        self.second_value = second_value
        self.second_degree = second_degree

        self.x_0 = np.array([[1], [1]])
        self.x_1 = Symbol('x_1')
        self.x_2 = Symbol('x_2')
        self.alpha = Symbol('alpha')

        self.y = self.first_value * self.x_1 ** self.first_degree + self.second_value * self.x_2 ** self.second_degree

    def calculate_s_0(self):
        s_0 = np.array([[-diff(self.y, self.x_1).subs(self.x_1, int(self.x_0[0]))],
                        [-diff(self.y, self.x_2).subs(self.x_2, int(self.x_0[1]))]])
        return s_0

    def calculate_alpha_0(self):
        alpha = self.x_0 + self.alpha * self.calculate_s_0()
        func = self.y.subs({self.x_1: alpha[0][0], self.x_2: alpha[1][0]})

        # Не прописан кейс, когда D > 0
        if self.second_value / self.first_value >= 10:
            return 1 / abs(self.calculate_s_0()[1][0])
        else:
            return 1 / abs(self.calculate_s_0()[0][0])

    def calculate_x1(self):
        return self.x_0 + self.calculate_alpha_0() * self.calculate_s_0()
