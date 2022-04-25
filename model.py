import random

class Linear:
    def  __init__(self):
        self.h_0 = random.uniform(-1, 1)
        self.grad_tape = []
        self.lr = 0.01

    def forward(self, x):
        y = self.h_0 * x
        self.grad_tape.append(x)
        return y

    def MSE(self, prediction, y):
        #error = numpy.power(prediction - y, 2) * (1/2)
        error = ((prediction - y) ** 2) * 0.5
        self.grad_tape.append(prediction - y)
        return error

    def zero_grad(self):
        self.grad_tape = []

    def backward(self):
        self.h_0 -= self.lr * self.grad_tape[0] * self.grad_tape[1]

    def summary(self):
        print(self.h_0)
