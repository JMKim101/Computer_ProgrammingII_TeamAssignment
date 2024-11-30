class Calc:
    def __init__(self, initial_value=0):
        self.result = initial_value

    def add(self, num):
        self.result = self.result + num
        return self.result
    
    def minus(self, num):
        self.result = self.result - num
        return self.result
    
    def setvalue(self, num):
        self.result = num
        return self.result
    
    def print(self):
        print(self.result)

    def getvalue(self):
        return self.result

cal1 = Calc()
cal2 = Calc(5)
cal1.setvalue(10)
cal1.add(20)
cal1.minus(5)
cal1.print()
cal2.add(cal1.getvalue())
cal2.print()



