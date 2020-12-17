import math
class Cal:
    def __init__(self, prior, signUsed, mathSignUsed):
        self.prior = prior
        self.signUsed = signUsed
        self.mathSignUsed = mathSignUsed
        self.answer = None
        self.lis = []

    def separator(self):
        separatedList = self.prior.split(self.mathSignUsed)
        if self.signUsed in separatedList[0]:
            if self.signUsed == "!":
                separateditem = separatedList[0][:-1]
                
                self.lis.append(math.factorial(int(separateditem)))

            elif self.signUsed == "√":
                separateditem = separatedList[0][1:]

                self.lis.append(math.sqrt(int(separateditem)))

        if self.signUsed in separatedList[1]:
            if self.signUsed == "!":
                separateditem = separatedList[0][:-1]
                
                self.lis.append(math.factorial(int(separateditem)))

            elif self.signUsed == "√":
                separateditem = separatedList[1][1:]

                self.lis.append(math.sqrt(int(separateditem)))

        if self.signUsed not in separatedList[0]:
            self.lis.append(separatedList[0])

        if self.signUsed not in separatedList[1]:
            self.lis.append(separatedList[1])

    def calculations(self):
        if self.mathSignUsed == "+":
            self.answer = int(self.lis[0]) + int(self.lis[1])

        elif self.mathSignUsed == "-":
            self.answer = int(self.lis[0]) - int(self.lis[1])

        elif self.mathSignUsed == "*":
            self.answer = int(self.lis[0]) * int(self.lis[1])

        else:
            self.answer = int(self.lis[0]) / int(self.lis[1])


    def result(self):
        self.separator()
        self.calculations()

        return self.answer