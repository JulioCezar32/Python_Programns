# project to start use python on the day by day
# this code only can be writen in english language

x = int(input("Insert the number of interaction to fibonacci \n"))

class Fibonacci:

    def __init__(self, x):
        self.x = x
        self.start = 0
        self.number = 1
        self.previous = 0

    def fibonacci(self):
        for i in range(0, self.x-1):
            self.previous = self.number
            self.number = self.start + self.previous
            self.start = self.previous
        return self.number

    def __str__(self):
       return "O valor da fibonaci é {}".format(self.number)


variable = Fibonacci(x)

print(variable)